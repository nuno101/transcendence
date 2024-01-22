from django.views import View
from django.utils.decorators import method_decorator
from .decorators import *
from django.http import JsonResponse, HttpResponse
from .models import User, FriendRequest
from .helpers_users import *
from .constants_ws_notification import *
from .constants_errors import *
from . import helpers_websocket as websocket

# Endpoint: /users/me
@method_decorator(login_required, name='dispatch')
class UserPersonal(View):
  def get(self, request):
    return JsonResponse({'user': request.user.serialize()}, status=200)
  
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
    return JsonResponse({'friends': [f.serialize() for f in friends]})

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

    websocket.send_user_notification(friend.id, REMOVE_FRIEND, {
      "user_id": request.user.id })
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
    return JsonResponse({"requests": [r.serialize() for r in friend_requests]})
  
  @check_body_syntax(['user_id'])
  def post(self, request): # TODO: Refactor this mess
    # Check if user exists
    try:
      target = User.objects.get(pk=self.body.get('user_id'))
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

    # Create friend request
    friend_request = FriendRequest(from_user=request.user, to_user=target)
    friend_request.save()

    websocket.send_user_notification(target.id, SEND_FRIEND_REQUEST, {
      "request": friend_request.serialize() })
    return JsonResponse({"request": friend_request.serialize()}, status=201)

# Endpoint: /users/me/friends/requests/<int:request_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(FriendRequest, 'request_id', 
                                      FRIEND_REQUEST_404), name='dispatch')
class FriendRequestSingle(View): # TODO: Refactor this mess?
  def post(self, request, request_id): # TODO: Refactor this mess
    friend_request = FriendRequest.objects.get(pk=request_id)

    # Check if user is the recipient of the request
    if friend_request.to_user.id != request.user.id:
      return JsonResponse({ERROR_FIELD: "User is not the recipient of the request"}, status=400)

    # Check if user is blocked
    if request.user.blocked.filter(id=friend_request.from_user.id).exists():
      return JsonResponse({ERROR_FIELD: "User is blocked"}, status=400)

    # Accept friend request
    request.user.friends.add(friend_request.from_user)
    from_user_id = friend_request.from_user.id
    friend_request.delete()

    websocket.send_user_notification(from_user_id, ACCEPT_FRIEND_REQUEST, {
      "user_id": request.user.id })
    return HttpResponse(status=204)

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
    websocket.send_user_notification(websocket_target.id, event, {
      "request_id": friend_request_id })
    return HttpResponse(status=204)

# Endpoint: /users/me/blocked
@method_decorator(login_required, name='dispatch')
class BlockedCollection(View):
  def get(self, request):
    blocked = request.user.blocked.all()
    return JsonResponse({"blocked": [b.serialize() for b in blocked]})

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

# Endpoint /users/me/channels
@method_decorator(login_required, name='dispatch')
class ChannelPersonal(View):
  def get(self, request):
    channels = Channel.objects.filter(members=request.user).order_by("-updated_at")
    return JsonResponse({'channels': [channel.serialize() for channel in channels]})