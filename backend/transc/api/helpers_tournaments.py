from .models import Tournament, Game

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
