from .models import Tournament, Game

# create a games for each player in the tournament
def create_games(tournament):
    for player in tournament.players.all():
        for opponent in tournament.players.all():
            if player != opponent:
                game = Game(
                    player1=player,
                    player2=opponent,
                    tournament=tournament
                )
                game.full_clean()
                game.save()