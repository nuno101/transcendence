# cCONF: Constants for endpoint structure

# Endpoint: /login
# Method: POST
class Login:
  class Post_params:
    PARAMS = [ "username", "password" ]
    PARAMS_OPTIONAL = []

# Endpoint: /logout
# Method: POST
class Logout:
  class Post_params:
    PARAMS = []
    PARAMS_OPTIONAL = []

# Endpoint: /users/me
# Method: GET, PATCH, DELETE
class Users_me:
  class Patch_params:
    PARAMS = ["nickname", "password"]
    PARAMS_OPTIONAL = []

# Endpoint: /users/me/avatar
# Method: POST
# TODO: Specify parameters
class Users_me_avatar:
  class Post_params:
    PARAMS = []
    PARAMS_OPTIONAL = []

# Endpoint: /users/me/blocked
# Method: GET, POST
class Users_me_blocked:
  class Post_params:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

# Endpoint: /users/me/blocked/<int:user_id>
# Method: DELETE
class Users_me_blocked_id:
  pass

# Endpoint: /users/me/channels
# Method: GET
class Users_me_channels:
  pass

# Endpoint: /users/me/friends
# Method: GET
class Users_me_friends:
  pass

# Endpoint: /users/me/friends/<int:user_id>
# Method: DELETE
class Users_me_friends_id:
  pass

# Endpoint: /users/me/friends/requests
# Method: GET, POST
class Users_me_friends_requests:
  class Post_params:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

# Endpoint: /users/me/friends/requests/<int:request_id>
# Method: POST, DELETE
class Users_me_friends_requests_id:
  class Post_params:
    PARAMS = []
    PARAMS_OPTIONAL = []

# Endpoint: /users/me/notifications
# Method: GET
class Users_me_notifications:
  pass

# Endpoint: /users/me/notifications/<int:notification_id>
# Method: DELETE
class Users_me_notifications_id:
  pass

# Endpoint: /users
# Method: GET, POST
class Users:
  class Post_params:
    PARAMS = ["username", "password"]
    PARAMS_OPTIONAL = []

# Endpoint: /users/<int:user_id>
# Method: GET, PATCH, DELETE
class Users_id:
  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["nickname", "password"]

# Endpoint: /users/<int:user_id>/avatar
# Method: GET
class Users_id_avatar:
  pass

# Endpoint: /users/<int:user_id>/stats
# Method: GET
class Users_id_stats:
  pass

# Endpoint: /users/<int:user_id>/games
# Method: GET
class Users_id_games:
  pass

# Endpoint: /tournaments
# Method: GET, POST
class Tournaments:
  class Post_params:
    PARAMS = ["title", "description"]
    PARAMS_OPTIONAL = []

# Endpoint: /tournaments/<int:tournament_id>
# Method: GET, PATCH, DELETE
class Tournaments_id:
  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["title", "description"]

# Endpoint: /games
# Method: GET, POST
class Games:
  class Post_params:
    PARAMS = ["tournament_id", "player1_id", "player2_id", "player1_score", "player2_score"]
    PARAMS_OPTIONAL = []

# Endpoint: /games/<int:game_id>
# Method: GET, PATCH, DELETE
class Games_id:
  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["player1_score", "player2_score", "status"]

# Endpoint: /channels
# Method: GET, POST
class Channels:
  class Post_params:
    PARAMS = ["name"]
    PARAMS_OPTIONAL = []

# Endpoint: /channels/<int:channel_id>
# Method: GET, PATCH, DELETE
class Channels_id:
  class Patch_params:
    PARAMS = []
    PARAMS_OPTIONAL = ["name"]

# Endpoint: /channels/<int:channel_id>/members
# Method: GET, PATCH
class Channels_id_members:
  class Patch_params:
    PARAMS = ["user_id"]
    PARAMS_OPTIONAL = []

# Endpoint: /channels/<int:channel_id>/members/<int:user_id>
# Method: DELETE
class Channels_id_members_id:
  pass

# Endpoint: /channels/<int:channel_id>/messages
# Method: GET, POST
class Channels_id_messages:
  class Post_params:
    PARAMS = ["content"]
    PARAMS_OPTIONAL = []

# Endpoint: /messages
# Method: GET
class Messages:
  pass

# Endpoint: /messages/<int:message_id>
# Method: PATCH, DELETE
class Messages_id:
  class Patch_params:
    PARAMS = [ 'content' ]
    PARAMS_OPTIONAL = []