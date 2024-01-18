from django.views import View
from django.utils.decorators import method_decorator
from .decorators import login_required, check_body_syntax, check_object_exists
from django.http import JsonResponse
from .models import User
import datetime

# GET   /users
# POST /users {"name": "dummy", "fullname": "Dummy user"}
class UserCollection(View):
	@method_decorator(login_required, name='dispatch')
	def get(self, request):
		users = User.objects.order_by("username")
		data = {
			'users': [u.serialize() for u in users],
			'count': users.count(),
		}
		return JsonResponse(data)

	# https://www.youtube.com/watch?v=i5JykvxUk_A
	@check_body_syntax(['username', 'fullname'])
	def post(self, request): # TODO: Add way to specify password
		user_data = {
			'username': self.body.get('username'),
			'fullname': self.body.get('fullname'),
			'created_at': datetime.datetime.now()
			}
		try:
			u = User.objects.create(**user_data)
		except:
			return JsonResponse({"reason": "User with username " +
													f"'{user_data.get('username')}' already exists"}, status=400)
		return JsonResponse(u.serialize(), status=201)

# GET    /users/<int:user_id>
# PATCH  /users/<int:user_id>
# DELETE /users/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', 
																			'User does not exist'), name='dispatch')
class SingleUser(View):
	def get(self, request, user_id):
		u = User.objects.get(pk=user_id)
		return JsonResponse({'user': u.serialize()}) # TODO: Maybe add safe=false and one level of nesting?
	
	@check_body_syntax(['username'])
	def patch(self, request, user_id):
		u = User.objects.get(pk=user_id)
		u.username = self.body.get('username')
		u.updated_at = datetime.datetime.now()
		try:
			u.save()
		except:
			return JsonResponse({"reason": "User with username " +
													 f"'{self.body.get('username')}' already exists"}, status=400)
		return JsonResponse(u.serialize(), status=200, safe=False)

	def delete(self, request, user_id):
		u = User.objects.get(pk=user_id)
		u.delete()
		return JsonResponse({}, status=202)
