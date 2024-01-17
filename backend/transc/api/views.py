from django.views import View
from django.http import JsonResponse
from .models import User
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
import datetime

def index(request):
	return JsonResponse({'response': "Hello, world. You're at the transcendence index."})

# GET   /users
# POST /users {"name": "dummy", "fullname": "Dummy user"}
class UserCollection(View):
	def get(self, request):
		users = User.objects.order_by("name")
		users_data = []
		for user in users:
			users_data.append(user.serialize())
		data = {
			'users': users_data,
			'count': users.count(),
		}
		return JsonResponse(data)

	# https://www.youtube.com/watch?v=i5JykvxUk_A
	def post(self, request):
		data = json.loads(request.body.decode("utf-8"))
		name = data.get('name')
		fullname = data.get('fullname')

		user_data = {
			'name':name,
			'fullname': fullname,
			'created_at': datetime.datetime.now()
			}

		u = User.objects.create(**user_data)
		return JsonResponse(u.serialize(), status=201)

# GET    /users/<int:user_id>
# PATCH  /users/<int:user_id>
# DELETE /users/<int:user_id>
class SingleUser(View):
	def get(self, request, user_id):
		try:
			u = User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return JsonResponse({"error": "404 Not found", "reason": "User does not exist"})
		return JsonResponse({'user': u.serialize()})
	
	# TODO: Implement PATCH and POST
