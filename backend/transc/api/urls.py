from django.urls import path
from . import views
from .views import TournamentView, TournamentDetail
from .views import GameView, GameDetail

urlpatterns = [
	path("", views.index, name="index"),
	path("users", views.user_list),
	path("users/", views.user_list),
	path("users/<int:user_id>", views.user_detail),
	path('tournaments/', TournamentView.as_view()),
	path('tournaments/<int:tournament_id>', TournamentDetail.as_view()),
	path('games/', GameView.as_view()),
	path('games/<int:game_id>', GameDetail.as_view()),
]

