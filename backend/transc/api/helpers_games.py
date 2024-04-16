from django.http import JsonResponse
from django.core.exceptions import ValidationError
import datetime
from .models import Game, Tournament, User
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
    players = tournament.players.all()
    initial_ranking = [{'user_id': player.id, 'points': None, 'wins': None, 'nickname': player.nickname} for player in players]
    tournament.ranking = initial_ranking
    for game in games:
      if game.status == Game.MatchStatus.DONE:
        player1 = game.player1
        player2 = game.player2
        player1_index = next((index for index, entry in enumerate(tournament.ranking) if entry['user_id'] == player1.id), None)
        player2_index = next((index for index, entry in enumerate(tournament.ranking) if entry['user_id'] == player2.id), None)
        if player1_index is not None and player2_index is not None:
          if game.player1_score > game.player2_score:
            tournament.ranking[player1_index]['wins'] = (tournament.ranking[player1_index].get('wins', 0) or 0) + 1
            tournament.ranking[player1_index]['points'] = (tournament.ranking[player1_index].get('points', 0) or 0) + (game.player1_score - game.player2_score)
            tournament.ranking[player2_index]['points'] = (tournament.ranking[player2_index].get('points', 0) or 0) - (game.player1_score - game.player2_score)
            if tournament.ranking[player2_index]['wins'] is None:
              tournament.ranking[player2_index]['wins'] = 0
          elif game.player2_score > game.player1_score:
            tournament.ranking[player2_index]['wins'] = (tournament.ranking[player2_index].get('wins', 0) or 0) + 1
            tournament.ranking[player2_index]['points'] = (tournament.ranking[player2_index].get('points', 0) or 0) + (game.player2_score - game.player1_score)
            tournament.ranking[player1_index]['points'] = (tournament.ranking[player1_index].get('points', 0) or 0) - (game.player2_score - game.player1_score)
            if tournament.ranking[player1_index]['wins'] is None:
              tournament.ranking[player1_index]['wins'] = 0

    for player_entry in tournament.ranking:
      if player_entry['wins'] is None:
        player_entry['wins'] = -1
        player_entry['points'] = -1

    # Sort ranking based on wins and points
    def custom_sort(player):
      return (-player['wins'], -player['points'])

    tournament.ranking.sort(key=custom_sort)

  tournament.save()

# Game serialization helpers
def get_user_games_done(user_id):
  games = Game.objects.filter((Q(player1=user_id) | Q(player2=user_id)) & Q(status=Game.MatchStatus.DONE) )
  games.order_by('-updated_at')
  return [g.serialize() for g in games]

