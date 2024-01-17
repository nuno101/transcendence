from django.urls import path
from . import views
from . import views_tournaments
from . import views_games

urlpatterns = [
	path("", views.index, name="index"),
  path("login", views.Login.as_view()),
	path("users", views.UserCollection.as_view()),
	path("users/", views.UserCollection.as_view()),
	path("users/<int:user_id>", views.SingleUser.as_view()),

	path('tournaments', views_tournaments.TournamentCollection.as_view()),
	path('tournaments/', views_tournaments.TournamentCollection.as_view()),
	path('tournaments/<int:tournament_id>', views_tournaments.TournamentSingle.as_view()),

	path('games/', views_games.GameView.as_view()),
	path('games/<int:game_id>', views_games.GameDetail.as_view()),
]
