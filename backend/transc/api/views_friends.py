from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError
from .decorators import *
from .models import User, FriendRequest
from .helpers_users import *
from . import helpers_notifications as notification
from .constants_websocket_events import *
from .constants_http_response import *
from . import bridge_websocket as websocket

# Endpoint: /users/me/friends
@method_decorator(check_structure("/users/me/friends"), name='dispatch')
class FriendCollection(View):
  def get(self, request):
    friends = request.user.friends.all()
    return JsonResponse([f.serialize(private=True) for f in friends], safe=False)

# Endpoint: /users/me/friends/USER_ID
@method_decorator(check_structure("/users/me/friends/USER_ID"), name='dispatch')
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
@method_decorator(check_structure("/users/me/friends/requests"), name='dispatch')
class FriendRequestCollection(View):
  # Get all friend requests, choose between sent and received
  def get(self, request):
    request_type = request.GET.get('type', None)
    if request_type == None:
      return JsonResponse({ERROR_FIELD: "Missing query parameter 'type'"}, status=400)
    
    if request_type == 'sent':
      friend_requests = FriendRequest.objects.filter(from_user=request.user)
    elif request_type == 'received':
      friend_requests = FriendRequest.objects.filter(to_user=request.user)
    return JsonResponse([r.serialize() for r in friend_requests], safe=False)

  # Create new friend request
  def post(self, request):
    try:
      target = User.objects.get(nickname=request.json.get('nickname'))
    except:
      return JsonResponse({ERROR_FIELD: USER_404}, status=404)

    # Check if you are trying to add yourself
    if target.id == request.user.id:
      return JsonResponse({ERROR_FIELD: "Cannot add yourself"}, status=400)

    # Check if user is blocked
    if request.user.blocked.filter(id=target.id).exists():
      return JsonResponse({ERROR_FIELD: "User is blocked"}, status=400)

    # Check if user is already a friend
    if request.user.friends.filter(id=target.id).exists():
      return JsonResponse({ERROR_FIELD: "User is already a friend"}, status=400)

    # Check if you are blocked by the user
    if target.blocked.filter(id=request.user.id).exists():
      return JsonResponse({ERROR_FIELD: "User blocked you"}, status=403)

    # Check if friend request was already sent
    if FriendRequest.objects.filter(from_user=request.user, to_user=target).exists():
      return JsonResponse({ERROR_FIELD: "Friend request already sent"}, status=400)

    # Check if friend request was already received
    if FriendRequest.objects.filter(from_user=target, to_user=request.user).exists():
      return JsonResponse({ERROR_FIELD: "Friend request already received"}, status=400)

    try:
      friend_request = FriendRequest(from_user=request.user, to_user=target)
      friend_request.full_clean()
      friend_request.save()
    except ValidationError as e:
      return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
    except Exception as e:
      return JsonResponse({ERROR_FIELD: str(e)}, status=500)

    websocket.send_user_event(target.id, CREATE_FRIEND_REQUEST, 
                              friend_request.serialize())

    return JsonResponse(friend_request.serialize(), status=201)

# Endpoint: /users/me/friends/requests/REQUEST_ID
@method_decorator(check_structure("/users/me/friends/requests/REQUEST_ID"), name='dispatch')
@method_decorator(check_object_exists(FriendRequest, 'request_id', 
                                      FRIEND_REQUEST_404), name='dispatch')
class FriendRequestSingle(View):
  # Accept friend request
  def post(self, request, request_id):
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

  # Decline or cancel friend request
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
