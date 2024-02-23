from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from django.views import View
from .decorators import *
from .models import Tournament, Game
from .models import User
from .helpers_tournaments import create_games
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import datetime

# Endpoint: /tournaments
@method_decorator(check_structure("/tournaments"), name='dispatch')
class TournamentCollection(View):
	def get(self, request):
		tournaments = Tournament.objects.all()
		return JsonResponse([t.serialize() for t in tournaments], safe=False)

	def post(self, request):
		try:
			tournament = Tournament(
				title=request.json.get('title'),
				description=request.json.get('description', ''),
				creator=request.user
			)
			tournament.full_clean()
			tournament.save()
			tournament.players.add(request.user)
		except ValidationError as e:
			return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
		except Exception as e:
			return JsonResponse({ERROR_FIELD: str(e)}, status=500)

		# TODO: Implement websocket notification?

		return JsonResponse(tournament.serialize(), status=201)

# Endpoint: /tournaments/TOURNAMENT_ID
@method_decorator(check_structure("/tournaments/TOURNAMENT_ID"), name='dispatch')
@method_decorator(check_object_exists(Tournament, 'tournament_id', TOURNAMENT_404), name='dispatch')
class TournamentSingle(View):

	def get(self, request, tournament_id):
		t = Tournament.objects.get(id=tournament_id)
		return JsonResponse(t.serialize())

	def patch(self, request, tournament_id):
		class TournamentStatus:
			CREATED = "created"
			REG_OPEN = "registration_open"
			REG_CLOSED = "registration_closed"
			ONGOING = "ongoing"
			DONE = "done"
			CANCELLED = "cancelled"
			states = [CREATED, REG_OPEN, REG_CLOSED, ONGOING, DONE, CANCELLED]

		tournament = Tournament.objects.get(id=tournament_id)
		# Only the creator can use this entrypoint
		if tournament.creator != request.user:
			return JsonResponse({ERROR_FIELD: TOURNAMENT_403}, status=403)
		
		if request.json.get('title') is not None:
			tournament.title = request.json.get('title')
		if request.json.get('description') is not None:
			tournament.description = request.json.get('description')
		if request.json.get('status') is not None:
			if request.json.get('status') == TournamentStatus.CANCELLED and \
				tournament.status != TournamentStatus.DONE and \
				tournament.status != TournamentStatus.CREATED and \
				tournament.status != TournamentStatus.ONGOING:
				tournament.status = TournamentStatus.CANCELLED
			elif request.json.get('status') == "next":
				next_status = TournamentStatus.states[TournamentStatus.states.index(tournament.status) + 1]
				if next_status == "registration_closed":
					if len(tournament.players.all()) < 2:
						return JsonResponse({ERROR_FIELD: "Not enough players"}, status=400)
					else:
						# Schedule games to be played. Scores are set to 0 by default
						create_games(tournament)
				# status done can not be triggered manually.
				# completion of all games will change tournament.status to done.
				elif next_status != "cancel" or next_status != "done":
					tournament.status = next_status
			else:
				return JsonResponse({ERROR_FIELD: "Invalid status"}, status=400)

		try:
			tournament.full_clean()
			tournament.save()
		except ValidationError as e:
			return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
		except Exception as e:
			return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)

		# TODO: Implement websocket notification?

		return JsonResponse(tournament.serialize())

	def delete(self, request, tournament_id):
		tournament = Tournament.objects.get(id=tournament_id)

		if tournament.creator != request.user:
			return JsonResponse({ERROR_FIELD: TOURNAMENT_403}, status=403)

		tournament.delete()

		# TODO: Implement websocket notification?

		return HttpResponse(status=204)
	

# Endpoint: /tournaments/TOURNAMENT_ID/join
@method_decorator(check_structure("/tournaments/TOURNAMENT_ID/play"), name='dispatch')
@method_decorator(check_object_exists(Tournament, 'tournament_id', TOURNAMENT_404), name='dispatch')

class TournamentSinglePlay(View):

	def post(self, request, tournament_id):
		tournament = Tournament.objects.get(id=tournament_id)
		if tournament.status != "registration_open":
			return JsonResponse({ERROR_FIELD: TOURNAMENT_403}, status=403)
				
		if request.json.get('play') == "join":
			tournament.players.add(request.user)
		elif request.json.get('play') == "unjoin":
			tournament.players.remove(request.user)

		try:
			tournament.full_clean()
			tournament.save()
		except ValidationError as e:
			return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
		except Exception as e:
			return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)

		return JsonResponse(tournament.serialize())