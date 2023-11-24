from django.urls import path
from . import views
from .views import TournamentView

urlpatterns = [
	path("", views.index, name="index"),
	path("users", views.user_list),
	path("users/", views.user_list),
	path("users/<int:user_id>", views.user_detail),
	path('tournaments/', TournamentView.as_view()),
]

