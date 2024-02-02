from django.utils.decorators import method_decorator
from .decorators import *
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Tournament
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import datetime

# Endpoint: /tournaments
class TournamentCollection(View):
	@method_decorator(staff_required, name='dispatch')
	def get(self, request):
		tournaments = Tournament.objects.all()
		return JsonResponse([t.serialize() for t in tournaments], safe=False)

	def post(self, request):
		tournament = Tournament.objects.create(
			title=self.body.get('title'),
			description=self.body.get('description', ''),
			creator=request.user
		)

		# TODO: Implement websocket notification?

		return JsonResponse(tournament.serialize(), status=201)

# Endpoint: /tournaments/<int:tournament_id>
@method_decorator(check_object_exists(Tournament, 'tournament_id', 
																			TOURNAMENT_404), name='dispatch')
class TournamentSingle(View):
	def get(self, request, tournament_id):
		t = Tournament.objects.get(id=tournament_id)
		return JsonResponse(t.serialize())

	def patch(self, request, tournament_id):
		tournament = Tournament.objects.get(id=tournament_id)
		if self.body.get('title') is not None:
			tournament.title = self.body.get('title')
		if self.body.get('description') is not None:
			tournament.description = self.body.get('description')
		tournament.save()

		# TODO: Implement websocket notification?

		return JsonResponse(tournament.serialize())

	@method_decorator(staff_required, name='dispatch')
	def delete(self, request, tournament_id):
		Tournament.objects.get(id=tournament_id).delete()

		# TODO: Implement websocket notification?

		return HttpResponse(status=204)
