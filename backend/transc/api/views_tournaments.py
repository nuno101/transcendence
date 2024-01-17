from django.utils.decorators import method_decorator
from .decorators import login_required, check_body_syntax, check_object_exists
from django.views import View
from django.http import JsonResponse
from .models import Tournament
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
import datetime

# GET /tournaments
# POST /tournaments
@method_decorator(login_required, name='dispatch')
class TournamentCollection(View):
	def get(self, request):
		tournaments = Tournament.objects.all()
		data = {
			'tournaments': [t.serialize() for t in tournaments],
			'count': tournaments.count(),
		}
		return JsonResponse(data) # TODO: Maybe add safe=false and one level of nesting?

	@check_body_syntax(["title", "description"])
	def post(self, request):
		tournament_data = {
				'title': self.body.get('title'),
				'description': self.body.get('description'),
				'creator_id': request.user.id,
				#'status': TournamentStatus::CREATED - set at DB level
				'created_at': datetime.datetime.now()
			}
		t = Tournament.objects.create(**tournament_data) # TODO: Check if creating is successful
		return JsonResponse(t.serialize(), status=201, safe=False)

#tournaments/<int:tournament_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Tournament, 'tournament_id', 
																			'Tournament does not exist'), name='dispatch')
class TournamentSingle(View):
	def get(self, request, tournament_id):
		t = Tournament.objects.get(pk=tournament_id)
		return JsonResponse({'tournament': t.serialize()}) # TODO: Maybe add safe=false and one level of nesting?

	# allow only update of title and description
	@check_body_syntax(["title", "description"])
	def patch(self, request, tournament_id):
		t = Tournament.objects.get(pk=tournament_id)
		t.title = self.body.get('title')
		t.description = self.body.get('description')
		t.updated_at = datetime.datetime.now()
		t.save()
		return JsonResponse(t.serialize(), status=200, safe=False)

	def delete(self, request, tournament_id):
		t = Tournament.objects.get(pk=tournament_id)
		t.delete()
		return JsonResponse({}, status=202)
