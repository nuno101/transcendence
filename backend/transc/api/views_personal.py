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
@method_decorator(check_structure("/users/me"), name='dispatch')
class UserPersonal(View):
  def get(self, request):
    return JsonResponse(request.user.serialize())
  
  def patch(self, request):
    return update_user(request.user, request.json)
  
  def delete(self, request):
    return delete_user(request.user)

# Endpoint: /users/me/avatar
@method_decorator(check_structure("/users/me/avatar"), name='dispatch')
class AvatarPersonal(View):
  def post(self, request):
    avatar = request.json.get('avatar')
    return update_avatar(request.user, avatar)

# Endpoint: /users/me/blocked
@method_decorator(check_structure("/users/me/blocked"), name='dispatch')
class BlockedCollection(View):
  def get(self, request):
    blocked = request.user.blocked.all()
    return JsonResponse([b.serialize() for b in blocked], safe=False)

  def post(self, request): # TODO: Refactor this mess
    try:
      target_user = User.objects.get(id=request.json.get('user_id'))
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

# Endpoint: /users/me/blocked/USER_ID
@method_decorator(check_structure("/users/me/blocked/USER_ID"), name='dispatch')
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
@method_decorator(check_structure("/users/me/channels"), name='dispatch')
class ChannelPersonal(View):
  def get(self, request):
    channels = Channel.objects.filter(members=request.user).order_by("-updated_at")
    return JsonResponse([channel.serialize() for channel in channels], safe=False)