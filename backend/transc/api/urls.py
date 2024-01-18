from django.urls import path
from . import views, views_games, views_tournaments, views_users

urlpatterns = [
	path("", views.index, name="index"),
  path("login", views.Login.as_view()),
  
	# User paths
	path("users", views_users.UserCollection.as_view()),
	path("users/<int:user_id>", views_users.SingleUser.as_view()),

	# Tournament paths
	path('tournaments', views_tournaments.TournamentCollection.as_view()),
	path('tournaments/<int:tournament_id>', views_tournaments.TournamentSingle.as_view()),

	# Game paths
	path('games', views_games.GameView.as_view()),
	path('games/<int:game_id>', views_games.GameDetail.as_view()),
]
