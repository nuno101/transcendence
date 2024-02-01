# cCONF: Constants for endpoint structure

class Login:
  endpoint = "/login"
  method = ["POST"]

  class Post_params:
    PARAMS = [ "username", "password" ]
    PARAMS_OPTIONAL = []

class Logout:
  endpoint = "/logout"
  method = ["POST"]

  class Post_params:
    PARAMS = []
    PARAMS_OPTIONAL = []

class Users_me:
  endpoint = "/users/me"
  method = ["GET", "PATCH", "DELETE"]

  class Patch_params:
    PARAMS = ["nickname", "password"]
    PARAMS_OPTIONAL = []

class Users_me_avatar:
  endpoint = "/users/me/avatar"
  method = ["POST"]

  # TODO: Specify parameters
  class Post_params:
    PARAMS = []
    PARAMS_OPTIONAL = []

class Users_me_blocked:
  endpoint = "/users/me/blocked"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

class Users_me_blocked_id:
  endpoint = "/users/me/blocked/<int:user_id>"
  method = ["DELETE"]

class Users_me_channels:
  endpoint = "/users/me/channels"
  method = ["GET"]

class Users_me_friends:
  endpoint = "/users/me/friends"
  method = ["GET"]

class Users_me_friends_id:
  endpoint = "/users/me/friends/<int:user_id>"
  method = ["DELETE"]

class Users_me_friends_requests:
  endpoint = "/users/me/friends/requests"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

class Users_me_friends_requests_id:
  endpoint = "/users/me/friends/requests/<int:request_id>"
  method = ["POST", "DELETE"]

  class Post_params:
    PARAMS = []
    PARAMS_OPTIONAL = []

class Users_me_notifications:
  endpoint = "/users/me/notifications"
  method = ["GET"]

class Users_me_notifications_id:
  endpoint = "/users/me/notifications/<int:notification_id>"
  method = ["DELETE"]

class Users:
  endpoint = "/users"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["username", "password"]
    PARAMS_OPTIONAL = []

class Users_id:
  endpoint = "/users/<int:user_id>"
  method = ["GET", "PATCH", "DELETE"]

  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["nickname", "password"]

class Users_id_avatar:
  endpoint = "/users/<int:user_id>/avatar"
  method = ["GET"]

class Users_id_stats:
  endpoint = "/users/<int:user_id>/stats"
  method = ["GET"]

class Users_id_games:
  endpoint = "/users/<int:user_id>/games"
  method = ["GET"]

class Tournaments:
  endpoint = "/tournaments"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["title", "description"]
    PARAMS_OPTIONAL = []

class Tournaments_id:
  endpoint = "/tournaments/<int:tournament_id>"
  method = ["GET", "PATCH", "DELETE"]

  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["title", "description"]

class Games:
  endpoint = "/games"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["tournament_id", "player1_id", "player2_id", "player1_score", "player2_score"]
    PARAMS_OPTIONAL = []

class Games_id:
  endpoint = "/games/<int:game_id>"
  method = ["GET", "PATCH", "DELETE"]

  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["player1_score", "player2_score", "status"]

class Channels:
  endpoint = "/channels"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["name"]
    PARAMS_OPTIONAL = []

class Channels_id:
  endpoint = "/channels/<int:channel_id>"
  method = ["GET", "PATCH", "DELETE"]

  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["name"]

class Channels_id_members:
  endpoint = "/channels/<int:channel_id>/members"
  method = ["GET", "PATCH"]

  class Patch_params:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

class Channels_id_members_id:
  endpoint = "/channels/<int:channel_id>/members/<int:user_id>"
  method = ["DELETE"]

class Channels_id_messages:
  endpoint = "/channels/<int:channel_id>/messages"
  method = ["GET", "POST"]

  class Post_params:
    PARAMS = ["content"]
    PARAMS_OPTIONAL = []

class Messages:
  endpoint = "/messages"
  method = ["GET"]

class Messages_id:
  endpoint = "/messages/<int:message_id>"
  method = ["PATCH", "DELETE"]

  class Patch_params:
    PARAMS = [ 'content' ]
    PARAMS_OPTIONAL = []