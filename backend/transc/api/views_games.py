from django.utils.decorators import method_decorator
from .decorators import login_required
from django.views import View
from django.http import JsonResponse, Http404
from .models import User
from .models import Game
#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
import datetime

# GET/POST  /games
@method_decorator(login_required, name='dispatch')
class GameView(View):
	def post(self, request):
		data = json.loads(request.body.decode("utf-8")) # TODO: Add error checking
		game_id = data.get('game_id')
		player_id = data.get('player_id')
		player2_id = data.get('player2_id')

		game_data = {
			'game_id': game_id,
			'player_id': player_id,
			'player2_id': player2_id,
			#'status': GameStatus::CREATED - set at DB level
			#'created_at': datetime.datetime.now()
		}

		t = Game.objects.create(**game_data)
		return JsonResponse(t.serialize(), status=201)

	def get(self, request):
		games = Game.objects.all()
		data = {
			'games': [g.serialize() for g in games],
			'count': games.count(),
		}
		return JsonResponse(data)

#games/<int:game_id>
@method_decorator(login_required, name='dispatch')
class GameDetail(View):
	def get(self, request, game_id):
		try:
			t = Game.objects.get(pk=game_id)
		except Game.DoesNotExist:
			raise Http404()
		return JsonResponse({'game': t.serialize()})

	# allow only update of title and description
	def patch(self, request, game_id):
		try: # TODO: Improve error checking
			data = json.loads(request.body.decode("utf-8"))
			t = Game.objects.get(pk=game_id)
			if (data.get('title')):
				t.title = data.get('title')
			if (data.get('description')):
				t.description = data.get('description')
			t.updated_at = datetime.datetime.now()
			t.save()

			return JsonResponse(t.serialize(), status=200, safe=False)
		except Game.DoesNotExist:
			raise Http404()

	def delete(self, request, game_id):
		try:
			t = Game.objects.get(pk=game_id)
			t.delete()
			return JsonResponse({}, status=202)
		except Game.DoesNotExist:
			raise Http404() # TODO: Improve error checking
