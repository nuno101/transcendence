from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
#from django.core.serializers import serialize
from .models import User
from .models import Tournament
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json

def index(request):
	return HttpResponse("Hello, world. You're at the transcendence index.")

def user_list(request):
	if request.method == 'GET':
		users = User.objects.order_by("name")
		users_data = []
		for user in users:
			users_data.append({
				'id': user.id,
				'name': user.name,
				'fullname': user.fullname,
			})
		data = {
			'users': users_data,
			'count': users.count(),
		}
		return JsonResponse(data)

	if request.method == 'POST':
		# https://www.youtube.com/watch?v=i5JykvxUk_A
		return JsonResponse({'TODO':'1'})

def user_detail(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		data = {'id': user.id,
				'name': user.name,
				'fullname': user.fullname,
				}
	except User.DoesNotExist:
		raise Http404()
	return JsonResponse({'user': data})

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
			#'status': TournamentStatus::CREATED
			'created_at': datetime.datetime.now()
		}

		tournament_item = Tournament.objects.create(**tournament_data)

		data = {
			"message": "New item added to Cart with id: {tournament_item.id}"
		}
		return JsonResponse(data, status=201)

	def get(self, request):
		tournaments = Tournament.objects.all()
		tournaments_data = []
		for t in tournaments:
			tournaments_data.append({
				'id': t.id,
				'title': t.title,
				'description': t.description,
				'creator_id': t.creator_id,
				#'status': t.status,
				'created_at': t.created_at,
			})
		data = {
			'tournaments': tournaments_data,
			'count': tournaments.count(),
		}
		return JsonResponse(data)

