from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from .decorators import login_required
from .models import User
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
import datetime

def index(request):
	return JsonResponse({'response': "Hello, world. You're at the transcendence index."})

class Login(View):
	def post(self, request):
		try: # TODO: Implement function decorator
			data = json.loads(request.body.decode("utf-8"))
		except:
			return JsonResponse({"reason": "Invalid Body syntax"}, status=400)
		try:
			username = data.get('name')
			password = data.get('password')
		except:
			return JsonResponse({"reason": "Required body parameter missing"}, status=400)
		user = authenticate(username=username, password=password)
		if user is None:
			return JsonResponse({"reason": "Invalid login credentials"}, status=401)
		login(request, user)
		return JsonResponse({'message': 'Login successful'})

# GET   /users
# POST /users {"name": "dummy", "fullname": "Dummy user"}
@method_decorator(login_required, name='dispatch')
class UserCollection(View):
	def get(self, request):
		users = User.objects.order_by("name")
		data = {
			'users': [u.serialize() for u in users],
			'count': users.count(),
		}
		return JsonResponse(data)

	# https://www.youtube.com/watch?v=i5JykvxUk_A
	def post(self, request):
		data = json.loads(request.body.decode("utf-8")) # TODO: status checking
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
@method_decorator(login_required, name='dispatch')
class SingleUser(View):
	def get(self, request, user_id):
		try:
			u = User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return JsonResponse({"reason": "User does not exist"}, status=404)
		return JsonResponse({'user': u.serialize()})
	
	# TODO: Implement PATCH and POST
