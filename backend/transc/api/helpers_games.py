from django.http import JsonResponse
from django.core.exceptions import ValidationError
import datetime
from .models import Game, Tournament
from .constants_http_response import *
from django.db.models import Q


# Game instance management helpers
def update_game(game: Game, parameters):
  try:
    if parameters.get('title') is not None:
      game.title = parameters.get('title')
    if parameters.get('description') is not None:
      game.title = parameters.get('description')
    game.full_clean()
    game.save()
  except ValidationError as e:
    return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
  except Exception as e:
    return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)
  
  # TODO: Implement websocket notification?

  return JsonResponse(game.serialize())

# Update tournament status if all games are done and/or cancelled
def update_tournament_status(tournament):
  games = Game.objects.filter(tournament=tournament)
  games_count = games.count()

  games_done = games.filter(status=Game.MatchStatus.DONE).count()
  games_cancelled = games.filter(status=Game.MatchStatus.CANCELLED).count()
  if games_count == (games_done + games_cancelled):
    tournament.status = Tournament.TournamentStatus.DONE
    tournament.save()

# Game serialization helpers
def get_user_games_done(user_id):
  games = Game.objects.filter((Q(player1=user_id) | Q(player2=user_id)) & Q(status=Game.MatchStatus.DONE) )
  games.order_by('-updated_at')
  return [g.serialize() for g in games]

