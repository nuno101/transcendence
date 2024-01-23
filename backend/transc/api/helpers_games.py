from django.http import JsonResponse
import datetime
from .models import Game
from .constants_errors import *

def update_game(game: Game, parameters):
  if parameters.get('title') is not None:
    game.title = parameters.get('title')
  if parameters.get('description') is not None:
    game.title = parameters.get('description')
  game.updated_at = datetime.datetime.now()
  try:
    game.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update game"}, status=500)
  
  # TODO: Implement websocket notification

  return JsonResponse(game.serialize())