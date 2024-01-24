from django.urls import path
from . import views, views_games, views_tournaments
from . import views_users, views_chat, views_personal

urlpatterns = [
	path("", views.index, name="index"),

  path("login", views.Login.as_view()),
  path("logout", views.Logout.as_view()),
  
	# TODO: Test new http to websocket bridge structure and see if it can be simplified
	path("test/websocket_log", views.websocket_log, name="websocket_log"), # TODO: DEBUG: Remove later
  path("test/websocket", views.websocket_custom, name="websocket"), # TODO: DEBUG: Remove later

	# Personal paths
  path("users/me", views_personal.UserPersonal.as_view()),
  
  path("users/me/friends", views_personal.FriendCollection.as_view()),
  path("users/me/friends/<int:user_id>", views_personal.FriendSingle.as_view()),
  
  path("users/me/friends/requests", views_personal.FriendRequestCollection.as_view()),
  path("users/me/friends/requests/<int:request_id>", views_personal.FriendRequestSingle.as_view()),
  
  path("users/me/blocked", views_personal.BlockedCollection.as_view()),
  path("users/me/blocked/<int:user_id>", views_personal.BlockedSingle.as_view()),

	path("users/me/channels", views_personal.ChannelPersonal.as_view()),

	# TODO: Add endpoints to list tournaments of current user?

	# User paths
	path("users", views_users.UserCollection.as_view()),
	path("users/<int:user_id>", views_users.UserSingle.as_view()),
	
	path("users/<int:user_id>/stats", views_users.StatsUser.as_view()), # TODO: Implement auto creation of UserStats object

  path("users/<int:user_id>/games", views_users.GameCollectionUser.as_view()), # TODO: Test

	# Tournament paths
	path('tournaments', views_tournaments.TournamentCollection.as_view()),
	path('tournaments/<int:tournament_id>', views_tournaments.TournamentSingle.as_view()),

	# Game paths
	path('games', views_games.GameView.as_view()),
	path('games/<int:game_id>', views_games.GameDetail.as_view()),

	# Chat paths
	path('channels', views_chat.ChannelCollection.as_view()),
	path('channels/<int:channel_id>', views_chat.ChannelSingle.as_view()),
  
	path('channels/<int:channel_id>/members', views_chat.ChannelMemberCollection.as_view()),
	path('channels/<int:channel_id>/members/<int:user_id>', views_chat.ChannelMemberSingle.as_view()),

	path('channels/<int:channel_id>/messages', views_chat.ChannelMessageCollection.as_view()),

	path('messages', views_chat.MessageCollection.as_view()),
	path('messages/<int:message_id>', views_chat.MessageSingle.as_view()),
]
