from django.utils.decorators import method_decorator
from .decorators import *
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Game, Tournament, User
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .helpers_games import update_game

# Endpoint: /games
@method_decorator(check_structure("/games"), name='dispatch')
class GameView(View):
	@method_decorator(staff_required, name='dispatch')
	def get(self, request):
		games = Game.objects.all()
		return JsonResponse([g.serialize() for g in games], safe=False)

	def post(self, request):
		try:
			tournament_id = request.json.get('tournament_id', None)
			tournament = None
			if tournament_id:
				tournament = Tournament.objects.get(id=tournament_id)
		except:
			return JsonResponse({ERROR_FIELD: TOURNAMENT_404}, status=404)
		try:
			player1 = User.objects.get(id=request.json.get('player1_id'))
			player2 = User.objects.get(id=request.json.get('player2_id'))
		except:
			return JsonResponse({ERROR_FIELD: USER_404}, status=404)
		if player1.id is player2.id:
			return JsonResponse({ERROR_FIELD: "You can't play against yourself"}, status=400)
		game = Game(tournament=tournament, player1=player1, player2=player2)
		game.player1_score = request.json.get('player1_score', 0)
		game.player2_score = request.json.get('player2_score', 0)
		game.save()

		# TODO: Implement websocket notification?

		return JsonResponse(game.serialize(), status=201)

# Endpoint: /games/GAME_ID
@method_decorator(check_structure("/games/GAME_ID"), name='dispatch')
@method_decorator(check_object_exists(Game, 'game_id', GAME_404), name='dispatch')
class GameDetail(View):

	def get(self, request, game_id):
		g = Game.objects.get(id=game_id)
		return JsonResponse(g.serialize())

	def patch(self, request, game_id):
		game = Game.objects.get(id=game_id)
		if game.player1_id != request.user.id and game.player2_id != request.user.id:
			return JsonResponse({ERROR_FIELD: "You are not a player in this game"}, status=400)
		return update_game(game, request.json)

	@method_decorator(staff_required, name='dispatch')
	def delete(self, request, game_id):
		Game.objects.get(id=game_id).delete()

		# TODO: Implement websocket notification?

		return HttpResponse(status=204)
