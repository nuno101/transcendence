from django.views import View
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from .decorators import *
from .models import User, FriendRequest, Channel
from .helpers_users import *
from .constants_websocket_events import *
from .constants_http_response import *
from . import bridge_websocket as websocket
import os

# Endpoint: /users/me
@method_decorator(check_structure("/users/me"), name='dispatch')
class UserPersonal(View):
  def get(self, request):
    return JsonResponse(request.user.serialize())
  
  def patch(self, request):
    return update_user(request.user, request.json)
  
  def delete(self, request):
    return delete_user(request.user)

# cCONF: Allowed avatar file extensions
ALLOWED_AVATAR_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'webp']

# Endpoint: /users/me/avatar
@method_decorator(check_structure("/users/me/avatar"), name='dispatch')
class AvatarPersonal(View):
  def post(self, request):
    avatar = request.FILES.get('avatar')
    if not avatar:
      return JsonResponse({ERROR_FIELD: "No avatar provided (needs to be a multipart/form-data field with key 'avatar')"}, status=400)
    extension = avatar.name.split('.')[-1]
    if extension not in ALLOWED_AVATAR_EXTENSIONS:
      return JsonResponse({ERROR_FIELD: f"Invalid file extension '{extension}'"}, status=400)

    # TODO: Delete old avatar if new one has different name

    try:
      request.user.avatar = avatar
      request.user.avatar.full_clean()
      request.user.save()
    except ValidationError as e:
      return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
    except Exception as e:
      return JsonResponse({ERROR_FIELD: str(e)}, status=500)

    return JsonResponse(request.user.serialize(), status=201)

# Endpoint: /users/me/blocked
@method_decorator(check_structure("/users/me/blocked"), name='dispatch')
class BlockedCollection(View):
  def get(self, request):
    blocked = request.user.blocked.all()
    return JsonResponse([b.serialize() for b in blocked], safe=False)

  def post(self, request):
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