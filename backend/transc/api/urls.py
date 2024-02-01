from django.urls import path
from . import views, views_games, views_tournaments
from . import views_users, views_chat, views_personal
from . import views_friends, views_notifications

urlpatterns = [
	path("", views.index, name="index"),

  path("login", views.Login.as_view()),
  path("logout", views.Logout.as_view()),
  
  path("test/websocket", views.websocket_custom, name="websocket"), # FIXME: DEBUG: Remove later

	# Personal paths
  path("users/me", views_personal.UserPersonal.as_view()),

	path("users/me/avatar", views_personal.AvatarPersonal.as_view()),

	path("users/me/blocked", views_personal.BlockedCollection.as_view()),
  path("users/me/blocked/<int:user_id>", views_personal.BlockedSingle.as_view()),

	path("users/me/channels", views_personal.ChannelPersonal.as_view()),

	# Friend paths
  path("users/me/friends", views_friends.FriendCollection.as_view()),
  path("users/me/friends/<int:user_id>", views_friends.FriendSingle.as_view()),
  
  path("users/me/friends/requests", views_friends.FriendRequestCollection.as_view()),
  path("users/me/friends/requests/<int:request_id>", views_friends.FriendRequestSingle.as_view()),

	# Notification paths
	path("users/me/notifications", views_notifications.NotificationCollection.as_view()),
	path("users/me/notifications/<int:notification_id>", views_notifications.NotificationSingle.as_view()),

	# TODO: Add endpoints to list tournaments of current user? Or do we just make them all public?

	# User paths
	path("users", views_users.UserCollection.as_view()),
	path("users/<int:user_id>", views_users.UserSingle.as_view()),

	path("users/<int:user_id>/avatar", views_users.UserAvatar.as_view()),
	
	path("users/<int:user_id>/stats", views_users.StatsUser.as_view()),

  path("users/<int:user_id>/games", views_users.GameCollectionUser.as_view()),

	# Tournament paths
	path('tournaments', views_tournaments.TournamentCollection.as_view()), # TODO: Make all turnaments public if we choose to not have a permission system
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
