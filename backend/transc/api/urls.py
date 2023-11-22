from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("test", views.test, name="test"),
	path("users", views.users, name="users"),
	path("<int:user_id>/", views.show, name="show"),
]

