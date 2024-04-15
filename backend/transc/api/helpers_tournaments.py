from .models import Tournament, Game
from . import bridge_websocket as websocket
from .constants_websocket_events import *

# create game among each registered players in the tournament
def create_games(tournament):
    scheduled = []
    for player in tournament.players.all():
        scheduled.append(player)
        for opponent in tournament.players.all():
            if opponent in scheduled:
                next
            elif player != opponent:
                game = Game(
                    player1=player,
                    player2=opponent,
                    tournament=tournament
                )
                game.full_clean()
                game.save()


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# send message to all registered players
def notify_players(tournament):
    for player in tournament.players.all():
        websocket.send_user_event(player.id, TOURNAMENT_STARTING, { "id": tournament.id})
