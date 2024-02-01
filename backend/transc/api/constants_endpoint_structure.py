# cCONF: Constants for url structure

class Login:
  url = "/login"

  class Post:
    PARAMS = [ "username", "password" ]
    PARAMS_OPTIONAL = []

class Logout:
  url = "/logout"

  class Post:
    PARAMS = []
    PARAMS_OPTIONAL = []

class Users_me:
  url = "/users/me"

  class Get:
    pass

  class Patch:
    PARAMS = ["nickname", "password"]
    PARAMS_OPTIONAL = []

  class Delete:
    pass

class Users_me_avatar:
  url = "/users/me/avatar"

  # TODO: Specify parameters
  class Post:
    PARAMS = []
    PARAMS_OPTIONAL = []

class Users_me_blocked:
  url = "/users/me/blocked"

  class Get:
    pass

  class Post:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

class Users_me_blocked_id:
  url = "/users/me/blocked/USER_ID"

  class Delete:
    pass

class Users_me_channels:
  url = "/users/me/channels"

  class Get:
    pass

class Users_me_friends:
  url = "/users/me/friends"

  class Get:
    pass

class Users_me_friends_id:
  url = "/users/me/friends/USER_ID"
  
  class Delete:
    pass

class Users_me_friends_requests:
  url = "/users/me/friends/requests"

  class Get:
    pass

  class Post:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

class Users_me_friends_requests_id:
  url = "/users/me/friends/requests/REQUEST_ID"

  class Post:
    PARAMS = []
    PARAMS_OPTIONAL = []

  class Delete:
    pass

class Users_me_notifications:
  url = "/users/me/notifications"
 
  class Get:
    pass

class Users_me_notifications_id:
  url = "/users/me/notifications/NOTIFICATION_ID"

  class Delete:
    pass

class Users:
  url = "/users"

  class Get:
    pass

  class Post:
    PARAMS = ["username", "password"]
    PARAMS_OPTIONAL = []

class Users_id:
  url = "/users/USER_ID"

  class Get:
    pass

  class Patch:
    PARAMS = []
    PARAMS_OPTIONAL = ["nickname", "password"]

  class Delete:
    pass

class Users_id_avatar:
  url = "/users/USER_ID/avatar"

  class Get:
    pass 

class Users_id_stats:
  url = "/users/USER_ID/stats"

  class Get:
    pass

class Users_id_games:
  url = "/users/USER_ID/games"

  class Get:
    pass

class Tournaments:
  url = "/tournaments"

  class Get:
    pass

  class Post:
    PARAMS = ["title", "description"]
    PARAMS_OPTIONAL = []

class Tournaments_id:
  url = "/tournaments/TOURNAMENT_ID"

  class Get:
    pass

  class Patch:
    PARAMS = []
    PARAMS_OPTIONAL = ["title", "description"]

class Games:
  url = "/games"

  class Get:
    pass

  class Post:
    PARAMS = ["tournament_id", "player1_id", "player2_id", "player1_score", "player2_score"]
    PARAMS_OPTIONAL = []

class Games_id:
  url = "/games/GAME_ID"

  class Get:
    pass

  class Patch:
    PARAMS = []
    PARAMS_OPTIONAL = ["player1_score", "player2_score", "status"]

  class Delete:
    pass

class Channels:
  url = "/channels"

  class Get:
    pass

  class Post:
    PARAMS = ["name"]
    PARAMS_OPTIONAL = []

class Channels_id:
  url = "/channels/CHANNEL_ID"

  class Get:
    pass

  class Patch:
    PARAMS = []
    PARAMS_OPTIONAL = ["name"]

  class Delete:
    pass

class Channels_id_members:
  url = "/channels/CHANNEL_ID/members"

  class Get:
    pass

  class Patch:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

class Channels_id_members_id:
  url = "/channels/CHANNEL_ID/members/USER_ID"

  class Delete:
    pass

class Channels_id_messages:
  url = "/channels/CHANNEL_ID/messages"

  class Get:
    pass

  class Post:
    PARAMS = ["content"]
    PARAMS_OPTIONAL = []

class Messages:
  url = "/messages"

  class Get:
    pass

class Messages_id:
  url = "/messages/MESSAGE_ID"

  class Patch:
    PARAMS = [ 'content' ]
    PARAMS_OPTIONAL = []
  
  class Delete:
    pass