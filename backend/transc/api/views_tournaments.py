from django.utils.decorators import method_decorator
from .decorators import login_required
from django.views import View
from django.http import JsonResponse, Http404
from .models import Tournament
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
import datetime

# GET /tournaments
# POST /tournaments
# GET  /tournaments/
# POST  /tournaments/
@method_decorator(login_required, name='dispatch')
class TournamentCollection(View):
	def get(self, request):
		tournaments = Tournament.objects.all()
		data = {
			'tournaments': [t.serialize() for t in tournaments],
			'count': tournaments.count(),
		}
		return JsonResponse(data)

	def post(self, request):
		try:
			data = json.loads(request.body.decode("utf-8"))
		except:
			return JsonResponse({"reason": "Invalid Body syntax"}, status=400)
		try:
			tournament_data = {
				'title': data.get('title'),
				'description': data.get('description'),
				'creator_id': request.user.id,
				#'status': TournamentStatus::CREATED - set at DB level
				'created_at': datetime.datetime.now()
			}
		except:
			return JsonResponse({"reason": "Required body parameter missing"}, status=400)
		t = Tournament.objects.create(**tournament_data)
		return JsonResponse(t.serialize(), status=201)

#tournaments/<int:tournament_id>
@method_decorator(login_required, name='dispatch')
class TournamentSingle(View):
	def get(self, request, tournament_id):
		try:
			t = Tournament.objects.get(pk=tournament_id)
		except Tournament.DoesNotExist:
			return JsonResponse({"reason": "Tournament does not exist"}, status=404)
		return JsonResponse({'tournament': t.serialize()})

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

			return JsonResponse(t.serialize(), status=200, safe=False)
		except Tournament.DoesNotExist:
			return JsonResponse({"reason": "Tournament does not exist"}, status=404)

	def delete(self, request, tournament_id):
		try:
			t = Tournament.objects.get(pk=tournament_id)
			t.delete()
			return JsonResponse({}, status=202)
		except Tournament.DoesNotExist:
			return JsonResponse({"reason": "Tournament does not exist"}, status=404)
