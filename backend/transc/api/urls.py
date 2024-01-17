from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("users", views.UserCollection.as_view()),
	path("users/", views.UserCollection.as_view()),
	path("users/<int:user_id>", views.SingleUser.as_view()),
	path('tournaments/', views.TournamentView.as_view()),
	path('tournaments/<int:tournament_id>', views.TournamentDetail.as_view()),
	path('games/', views.GameView.as_view()),
	path('games/<int:game_id>', views.GameDetail.as_view()),
]

