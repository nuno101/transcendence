from django.views import View
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.password_validation import validate_password
from django.db.models import Q
from .decorators import *
from .models import User, Game
from .helpers_users import update_user
from .helpers_games import get_user_games_done

# Endpoint: /users
@method_decorator(check_structure("/users"), name='dispatch')
class UserCollection(View):
	def get(self, request):
		users = User.objects.order_by("username")
		return JsonResponse([u.serialize() for u in users], safe=False)

	def post(self, request):
		try:
			user = User(username=request.json.get('username'), nickname=request.json.get('username'))
			password = request.json.get('password')
			try:
					validate_password(password, user)
			except Exception as e:
					return JsonResponse({ERROR_FIELD: "Password too easy"}, status=400)
			user.set_password(password)	
			user.full_clean()
			user.save()
		except ValidationError as e:
			error_object = e.message_dict
			return JsonResponse({"type": "object", ERROR_FIELD: error_object}, status=400)
		except Exception as e:
			return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)

		return JsonResponse(user.serialize(private=True), status=201)

# Endpoint: /users/USER_ID
@method_decorator(check_structure("/users/USER_ID"), name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class UserSingle(View):
	def get(self, request, user_id):
		u = User.objects.get(id=user_id)
		response = JsonResponse(u.serialize())
		response['Cache-Control'] = 'no-store, no-cache, must-revalidate'
		response['Pragma'] = 'no-cache'
		response['Expires'] = '0'
		return response

	@method_decorator(staff_required, name='dispatch')
	def patch(self, request, user_id):
		return update_user(User.objects.get(id=user_id), request.json)

	@method_decorator(staff_required, name='dispatch')
	def delete(self, request, user_id):
		User.objects.get(id=user_id).delete()
		return HttpResponse(status=204)

# Endpoint: /users/USER_ID/avatar
@method_decorator(check_structure("/users/USER_ID/avatar"), name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class AvatarUser(View):
	def get(self, request, user_id):
		u = User.objects.get(id=user_id)
		url = u.get_avatar_url()
		ext = url.split('.')[-1]
		response = HttpResponse(status=301, headers={'Location': url})
		response['Cache-Control'] = 'no-store, no-cache, must-revalidate'
		response['Pragma'] = 'no-cache'
		response['Expires'] = '0'
		return response

# Endpoint: /users/USER_ID/games
@method_decorator(check_structure("/users/USER_ID/games"), name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class GameCollectionUser(View):
	def get(self, request, user_id):
		games = get_user_games_done(user_id)
		return JsonResponse(games, safe=False)
	
# Endpoint: /users/USER_ID/games_upcoming
@method_decorator(check_structure("/users/USER_ID/games_upcoming"), name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', USER_404), name='dispatch')
class GameCollectionUserUpcoming(View):
	def get(self, request, user_id):
		games = Game.objects.filter((Q(player1=user_id) | Q(player2=user_id)) & Q(status=Game.MatchStatus.CREATED) )
		games.order_by('-updated_at')
		return JsonResponse([g.serialize() for g in games], safe=False)