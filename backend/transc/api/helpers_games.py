from django.http import JsonResponse
import datetime
from .models import Game
from .constants_http_response import *
from django.db.models import Q

# Game instance management helpers
def update_game(game: Game, parameters):
  try:
    if parameters.get('title') is not None:
      game.title = parameters.get('title')
    if parameters.get('description') is not None:
      game.title = parameters.get('description')
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update game"}, status=500)
  
  # TODO: Implement websocket notification

  return JsonResponse(game.serialize())

# Game serialization helpers
def get_user_games(user_id):
  games = Game.objects.filter(Q(player1=user_id) | Q(player2=user_id))
  games.order_by('-updated_at')
  return [g.serialize() for g in games]