from django.views import View
from django.utils.decorators import method_decorator
from .decorators import *
from django.http import JsonResponse
from .models import User
from .helpers_users import update_user

# Endpoint: /users
class UserCollection(View):
	@login_required
	@staff_required
	def get(self, request):
		users = User.objects.order_by("username")
		data = {
			'users': [u.serialize() for u in users],
			'count': users.count(),
		}
		return JsonResponse(data)

	@check_body_syntax(['username', 'password'])
	def post(self, request):
		try:
			u = User.objects.create_user(username=self.body.get('username'), 
																	 password=self.body.get('password'))
		except:
			return JsonResponse({"reason": "User with username " +
													f"'{self.body.get('username')}' already exists"}, status=400)
		return JsonResponse({'user': u.serialize()}, status=201)

# Endpoint: /users/<int:user_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(User, 'user_id', 
																			'User does not exist'), name='dispatch')
class UserSingle(View):
	def get(self, request, user_id):
		u = User.objects.get(pk=user_id)
		return JsonResponse({'user': u.serialize()})
	
	@staff_required
	@check_body_syntax([])
	def patch(self, request, user_id):
		return update_user(User.objects.get(pk=user_id), request.body)

	@staff_required
	def delete(self, request, user_id):
		User.objects.get(pk=user_id).delete()
		return JsonResponse({}, status=204)
