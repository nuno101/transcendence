from django.views import View
from django.utils.decorators import method_decorator
from .decorators import *
from django.http import JsonResponse, HttpResponse
from .models import User, FriendRequest
from .helpers_users import *
from .constants_websocket_events import *
from .constants_http_response import *
from . import bridge_websocket as websocket

# Endpoint: /users/me
@method_decorator(login_required, name='dispatch')
class UserPersonal(View):
  def get(self, request):
    return JsonResponse(request.user.serialize())
  
  @check_body_syntax([])
  def patch(self, request):
    return update_user(request.user, self.body)
  
  def delete(self, request):
    return delete_user(request.user)

# Endpoint: /users/me/friends
@method_decorator(login_required, name='dispatch')
class FriendCollection(View):
  def get(self, request):
    friends = request.user.friends.all()
    return JsonResponse([f.serialize(private=True) for f in friends], safe=False)

# Endpoint: /users/me/friends/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class FriendSingle(View):
  def delete(self, request, user_id):
    friend = User.objects.get(pk=user_id)

    # Check if user is a friend
    if not request.user.friends.filter(id=user_id).exists():
      return JsonResponse({ERROR_FIELD: "User is not a friend"}, status=400)
    request.user.friends.remove(friend)

    websocket.send_user_event(friend.id, REMOVE_FRIEND, {
      "id": request.user.id })
    return HttpResponse(status=204)

# Endpoint: /users/me/friends/requests
@method_decorator(login_required, name='dispatch')
class FriendRequestCollection(View):
  def get(self, request):
    request_type = request.GET.get('type', None)
    if request_type == None:
      return JsonResponse({ERROR_FIELD: "Missing query parameter 'type'"}, status=400)
    
    if request_type == 'sent':
      friend_requests = FriendRequest.objects.filter(from_user=request.user)
    elif request_type == 'received':
      friend_requests = FriendRequest.objects.filter(to_user=request.user)
    else:
      return JsonResponse({ERROR_FIELD: "Invalid query parameter 'type'"}, status=400)
    return JsonResponse([r.serialize() for r in friend_requests], safe=False)
  
  @check_body_syntax(['username'])
  def post(self, request): # TODO: Refactor this mess?
    # Check if user exists
    try:
      target = User.objects.get(username=self.body.get('username'))
    except:
      return JsonResponse({ERROR_FIELD: USER_404}, status=404)

    # Check if you are trying to add yourself
    if target.id == request.user.id:
      return JsonResponse({ERROR_FIELD: "Cannot add yourself"}, status=400)

    # Check if user is already a friend or blocked
    if request.user.blocked.filter(id=target.id).exists():
      return JsonResponse({ERROR_FIELD: "User is blocked"}, status=400)
    if request.user.friends.filter(id=target.id).exists():
      return JsonResponse({ERROR_FIELD: "User is already a friend"}, status=400)

    # Check if you are blocked by the user
    if target.blocked.filter(id=request.user.id).exists():
      return JsonResponse({ERROR_FIELD: "User blocked you"}, status=403)

    # Check if friend request was already sent
    if FriendRequest.objects.filter(from_user=request.user, to_user=target).exists():
      return JsonResponse({ERROR_FIELD: "Friend request already sent"}, status=400)

    friend_request = FriendRequest.objects.create(from_user=request.user, to_user=target)

    websocket.send_user_event(target.id, CREATE_FRIEND_REQUEST, 
                              friend_request.serialize())
    return JsonResponse(friend_request.serialize(), status=201)

# Endpoint: /users/me/friends/requests/<int:request_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(FriendRequest, 'request_id', 
                                      FRIEND_REQUEST_404), name='dispatch')
class FriendRequestSingle(View):
  def patch(self, request, request_id):
    friend_request = FriendRequest.objects.get(pk=request_id)

    # Check if user is the recipient of the request
    if friend_request.to_user.id != request.user.id:
      return JsonResponse({ERROR_FIELD: "User is not the recipient of the request"}, status=400)

    # Check if user is blocked
    if request.user.blocked.filter(id=friend_request.from_user.id).exists():
      return JsonResponse({ERROR_FIELD: "User is blocked"}, status=400)

    # Accept friend request
    request.user.friends.add(friend_request.from_user)

    from_user = friend_request.from_user
    websocket.send_user_event(from_user.id, ACCEPT_FRIEND_REQUEST, 
                              friend_request.serialize())
    friend_request.delete()
    return JsonResponse(from_user.serialize(private=True), status=201)

  def delete(self, request, request_id):
    friend_request = FriendRequest.objects.get(pk=request_id)

    # Check if user is the recipient or sender of the request
    sender = friend_request.from_user.id == request.user.id
    recipient = friend_request.to_user.id == request.user.id
    if not sender and not recipient:
      return JsonResponse({ERROR_FIELD: FRIEND_REQUEST_403}, status=403)
    
    friend_request_id = friend_request.id
    friend_request.delete()

    websocket_target = friend_request.to_user if sender else friend_request.from_user

    event = CANCEL_FRIEND_REQUEST if sender else DECLINE_FRIEND_REQUEST
    websocket.send_user_event(websocket_target.id, 
                              event, {"id": friend_request_id })
    return HttpResponse(status=204)

# Endpoint: /users/me/blocked
@method_decorator(login_required, name='dispatch')
class BlockedCollection(View):
  def get(self, request):
    blocked = request.user.blocked.all()
    return JsonResponse([b.serialize() for b in blocked], safe=False)

  @check_body_syntax(['user_id'])  
  def post(self, request): # TODO: Refactor this mess
    try:
      target_user = User.objects.get(pk=self.body.get('user_id'))
    except:
      return JsonResponse({ERROR_FIELD: USER_404}, status=404)
    
    # Check if user is trying to block themselves
    if target_user.id == request.user.id:
      return JsonResponse({ERROR_FIELD: "Cannot block yourself"}, status=400)
    
    # Check if user is already blocked
    if request.user.blocked.filter(id=target_user.id).exists():
      return JsonResponse({ERROR_FIELD: "User is already blocked"}, status=400)
    
    # Check if user is already a friend
    if request.user.friends.filter(id=target_user.id).exists():
      return JsonResponse({ERROR_FIELD: "User is a friend"}, status=400)
    
    # Check if there is a outgoing friend request
    if FriendRequest.objects.filter(from_user=request.user, to_user=target_user).exists():
      return JsonResponse({ERROR_FIELD: "Outgoing friend request exists"}, status=400)

    # Check if there is a incoming friend request
    incoming_request = FriendRequest.objects.filter(from_user=target_user, to_user=request.user)
    if incoming_request.exists():
      incoming_request.delete()

    # TODO: Delete all channels with only the blocked user and the current user
    # TODO: Implement websocket notification

    # Block user
    request.user.blocked.add(target_user)

    return HttpResponse(status=204)

# Endpoint: /users/me/blocked/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class BlockedSingle(View):
  def delete(self, request, user_id):
    blocked = User.objects.get(pk=user_id)

    # Check if user is blocked
    if not request.user.blocked.filter(id=user_id).exists():
      return JsonResponse({ERROR_FIELD: "User is not blocked"}, status=400)
    request.user.blocked.remove(blocked)
    return HttpResponse(status=204)

# Endpoint: /users/me/channels
@method_decorator(login_required, name='dispatch')
class ChannelPersonal(View):
  def get(self, request):
    channels = Channel.objects.filter(members=request.user).order_by("-updated_at")
    return JsonResponse([channel.serialize() for channel in channels], safe=False)