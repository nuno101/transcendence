from django.views import View
from django.http import JsonResponse, Http404
from .models import User
from .models import Tournament
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .serials import serialize_user, serialize_tournament
import json
import datetime

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

