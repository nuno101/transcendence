from django.views import View
from django.utils.decorators import method_decorator
from .decorators import *
from django.http import JsonResponse
from .models import User, FriendRequest
from .helpers_users import update_user

# Endpoint: /users/me
@method_decorator(login_required, name='dispatch')
class UserPersonal(View):
  def get(self, request):
    return JsonResponse({'user': request.user.serialize()}, status=200)
  
  @check_body_syntax([])
  def patch(self, request):
    return update_user(request.user, request.body)
  
  def delete(self, request):
    request.user.delete()
    return JsonResponse({}, status=204)

# Endpoint: /users/me/friends
@method_decorator(login_required, name='dispatch')
class FriendCollection(View): # TODO: Complete request methods
  def get(self, request):
    friends = request.user.friends.all()
    return JsonResponse([f.serialize() for f in friends], status=200)

# Endpoint: /users/me/friends/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', 
																			'User does not exist'), name='dispatch')
class FriendSingle(View): # TODO: Complete request methods (delete)
  def delete(self, request, user_id):
    pass

# Endpoint: /users/me/friends/requests
@method_decorator(login_required, name='dispatch')
class FriendRequestCollection(View): # TODO: Complete request methods (post?)
  def get(self, request):
    requests = FriendRequest.objects.filter(to_user=request.user)
    return JsonResponse([r.serialize() for r in requests], status=200)

# Endpoint: /users/me/blocked
@method_decorator(login_required, name='dispatch')
class BlockedCollection(View):  # TODO: Complete request methods (post)
  def get(self, request):
    blocked = request.user.blocked.all()
    return JsonResponse([b.serialize() for b in blocked], status=200)
  
  def post(self, request):
    pass

# Endpoint: /users/me/blocked/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', 
																			'User does not exist'), name='dispatch')
class BlockedSingle(View):  # TODO: Complete request methods (delete)
  def delete(self, request, user_id):
    pass