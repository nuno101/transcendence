from django.http import JsonResponse
from django.core.exceptions import ValidationError
import datetime
from .models import Game, Tournament
from .constants_http_response import *
from django.db.models import Q

# Update tournament status if all games are done and/or cancelled
def update_tournament_status(tournament):
  games = Game.objects.filter(tournament=tournament)
  games_count = games.count()

  games_done = games.filter(status=Game.MatchStatus.DONE).count()
  games_cancelled = games.filter(status=Game.MatchStatus.CANCELLED).count()
  if games_count == games_cancelled and games_done == 0:
    tournament.status = Tournament.TournamentStatus.CANCELLED
    tournament.save()
  elif games_count == (games_done + games_cancelled):
    tournament.status = Tournament.TournamentStatus.DONE
    tournament.save()

# Game serialization helpers
def get_user_games_done(user_id):
  games = Game.objects.filter((Q(player1=user_id) | Q(player2=user_id)) & Q(status=Game.MatchStatus.DONE) )
  games.order_by('-updated_at')
  return [g.serialize() for g in games]

