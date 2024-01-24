from django.views import View
from django.utils.decorators import method_decorator
from .decorators import *
from django.http import JsonResponse, HttpResponse
from .models import User, UserStats, Game
from django.db.models import Q
from .helpers_users import update_user
from .helpers_games import get_user_games

# Endpoint: /users
class UserCollection(View):
	@method_decorator(login_required, name='dispatch')
	@method_decorator(staff_required, name='dispatch')
	def get(self, request):
		users = User.objects.order_by("username")
		return JsonResponse([u.serialize() for u in users], safe=False)

	@check_body_syntax(['username', 'password'])
	def post(self, request):
		try:
			user = User.objects.create_user(username=self.body.get('username'), 
																			password=self.body.get('password'))
		except Exception as e:
			if 'duplicate key' in str(e):
				return JsonResponse({ERROR_FIELD: "Username already taken"}, status=400)
			else:
				return JsonResponse({ERROR_FIELD: "Undefined error"}, status=400)
		return JsonResponse(user.serialize(), status=201)

# Endpoint: /users/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class UserSingle(View):
	def get(self, request, user_id):
		u = User.objects.get(pk=user_id)
		return JsonResponse(u.serialize())
	
	@method_decorator(staff_required, name='dispatch')
	@check_body_syntax([])
	def patch(self, request, user_id):
		return update_user(User.objects.get(pk=user_id), self.body)

	@method_decorator(staff_required, name='dispatch')
	def delete(self, request, user_id):
		User.objects.get(pk=user_id).delete()
		return HttpResponse(status=204)

# Endpoint: /users/<int:user_id>/stats
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class StatsUser(View):
	def get(self, request, user_id):
		u = User.objects.get(pk=user_id)
		return JsonResponse(u.stats.serialize())

# Endpoint: /users/<int:user_id>/games
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class GameCollectionUser(View):
	def get(self, request, user_id):
		games = get_user_games(user_id)
		return JsonResponse(games, safe=False)
