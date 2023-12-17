from django.views import View
from django.http import JsonResponse, Http404
from .models import User
from .models import Tournament
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .serials import serialize_user, serialize_tournament
from .views_tournaments import TournamentView, TournamentDetail
import json
import datetime

def index(request):
	return JsonResponse({'response': "Hello, world. You're at the transcendence index."})

# GET   /users
# POST /users {"name": "dummy", "fullname": "Dummy user"}
def user_list(request):
	if request.method == 'GET':
		users = User.objects.order_by("name")
		users_data = []
		for user in users:
			users_data.append(serialize_user(user))
		data = {
			'users': users_data,
			'count': users.count(),
		}
		return JsonResponse(data)

	# https://www.youtube.com/watch?v=i5JykvxUk_A
	if request.method == 'POST':
		data = json.loads(request.body.decode("utf-8"))
		name = data.get('name')
		fullname = data.get('fullname')

		user_data = {
			'name':name,
			'fullname': fullname,
			'created_at': datetime.datetime.now()
			}

		u = User.objects.create(**user_data)
		u = serialize_user(user)
		return JsonResponse(u, status=201)

# GET    /users/<int:user_id>
# PATCH  /users/<int:user_id>
# DELETE /users/<int:user_id>
def user_detail(request, user_id):
	try:
		u = User.objects.get(pk=user_id)
	except User.DoesNotExist:
		raise Http404()
	return JsonResponse({'user': serialize_user(u)})

