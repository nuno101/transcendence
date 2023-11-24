from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("test", views.test, name="test"),
	path("users", views.user_list),
	path("users/<int:user_id>", views.user_detail),
]

