from django.utils.decorators import method_decorator
from .decorators import *
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Game, Tournament, User
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import datetime

# /games
@method_decorator(login_required, name='dispatch')
class GameView(View):
	@method_decorator(staff_required, name='dispatch')
	def get(self, request):
		games = Game.objects.all()
		data = {
			'games': [g.serialize() for g in games],
			'count': games.count(),
		}
		return JsonResponse(data)

	@check_body_syntax(['tournament_id', 'player_id', 'player2_id'])
	def post(self, request):
		try:
			tournament = Tournament.objects.get(pk=self.body.get('tournament_id'))
		except:
			return JsonResponse({ERROR_FIELD: TOURNAMENT_404}, status=404)
		try:
			player1 = User.objects.get(pk=self.body.get('player_id'))
			player2 = User.objects.get(pk=self.body.get('player2_id'))
		except:
			return JsonResponse({ERROR_FIELD: USER_404}, status=404)
		game = Game(tournament=tournament, player1=player1, player2=player2)
		game.save()
		return JsonResponse({'game': game.serialize()}, status=201)

# /games/<int:game_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Game, 'game_id', GAME_404), name='dispatch')
class GameDetail(View):
	def get(self, request, game_id):
		g = Game.objects.get(pk=game_id)
		return JsonResponse({'game': g.serialize()})

	@check_body_syntax(['title', 'description'])
	def patch(self, request, game_id):
		g = Game.objects.get(pk=game_id)
		g.title = self.body.get('title')
		g.description = self.body.get('description')
		g.updated_at = datetime.datetime.now()
		g.save()
		return JsonResponse(g.serialize(), status=200, safe=False)

	@method_decorator(staff_required, name='dispatch')
	def delete(self, request, game_id):
		Game.objects.get(pk=game_id).delete()
		return HttpResponse(status=204)
