from django.views import View
from django.http import JsonResponse, Http404
from .models import User
from .models import Tournament
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .serials import serialize_user, serialize_tournament
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

# GET/POST  /tournaments
class TournamentView(View):
	def post(self, request):
		data = json.loads(request.body.decode("utf-8"))
		title = data.get('title')
		description = data.get('description')
		creator_id = data.get('creator_id')

		tournament_data = {
			'title': title,
			'description': description,
			'creator_id': creator_id,
			#'status': TournamentStatus::CREATED - set at DB level
			'created_at': datetime.datetime.now()
		}

		t = Tournament.objects.create(**tournament_data)
		return JsonResponse(serialize_tournament(t), status=201)

	def get(self, request):
		tournaments = Tournament.objects.all()
		tournaments_data = []
		for t in tournaments:
			tournaments_data.append(serialize_tournament(t))
		data = {
			'tournaments': tournaments_data,
			'count': tournaments.count(),
		}
		return JsonResponse(data)

#tournaments/<int:tournament_id>
class TournamentDetail(View):
	def get(self, request, tournament_id):
		try:
			t = Tournament.objects.get(pk=tournament_id)
		except Tournament.DoesNotExist:
			raise Http404()
		return JsonResponse({'tournament': serialize_tournament(t)})

	# allow only update of title and description
	def patch(self, request, tournament_id):
		try:
			data = json.loads(request.body.decode("utf-8"))
			t = Tournament.objects.get(pk=tournament_id)
			if (data.get('title')):
				t.title = data.get('title')
			if (data.get('description')):
				t.description = data.get('description')
			t.updated_at = datetime.datetime.now()
			t.save()

			return JsonResponse(serialize_tournament(t), status=200, safe=False)
		except Tournament.DoesNotExist:
			raise Http404()

	def delete(self, request, tournament_id):
		try:
			t = Tournament.objects.get(pk=tournament_id)
			t.delete();
			return JsonResponse({}, status=202)
		except Tournament.DoesNotExist:
			raise Http404()

