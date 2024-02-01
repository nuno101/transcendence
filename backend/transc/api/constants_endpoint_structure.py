# cCONF: Constants for url structure

class Login:
  url = "/login"

  class Post:
    PARAMS = [ {
      "name": "username",
      "type": "string",
      "required": True,
      "description": "Username of the user"
    }, {
      "name": "password",
      "type": "string",
      "required": True,
      "description": "Password of the user"
    } ]

class Logout:
  url = "/logout"

  class Post:
    PARAMS = []

class Users_me:
  url = "/users/me"

  class Get:
    pass

  class Patch:
    PARAMS = [
      {
        "name": "nickname",
        "type": "string",
        "required": False,
        "description": "Nickname of the user"
      }, {
        "name": "password",
        "type": "string",
        "required": False,
        "description": "Password of the user"
      }
    ]

  class Delete:
    pass

class Users_me_avatar:
  url = "/users/me/avatar"

  # TODO: Specify parameters
  class Post:
    PARAMS = []

class Users_me_blocked:
  url = "/users/me/blocked"

  class Get:
    pass

  class Post:
    PARAMS = [
      {
        "name": "user_id",
        "type": "id",
        "required": True,
        "description": "ID of the user to block"
      }
    ]

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
    PARAMS = [
      {
        "name": "username",
        "type": "string",
        "required": True,
        "description": "Username of the to send the friend request to"
      }
    ]

class Users_me_friends_requests_id:
  url = "/users/me/friends/requests/REQUEST_ID"

  class Post:
    PARAMS = []

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
    PARAMS = [
      {
        "name": "username",
        "type": "string",
        "required": True,
        "description": "Username of the user"
      }, {
        "name": "password",
        "type": "string",
        "required": True,
        "description": "Password of the user"
      }
    ]

class Users_id:
  url = "/users/USER_ID"

  class Get:
    pass

  class Patch:
    PARAMS = [
      {
        "name": "nickname",
        "type": "string",
        "required": False,
        "description": "Nickname of the user"
      }, {
        "name": "password",
        "type": "string",
        "required": False,
        "description": "Password of the user"
      }
    ]

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
    PARAMS = [
      {
        "name": "title",
        "type": "string",
        "required": True,
        "description": "Title of the tournament"
      }, {
        "name": "description",
        "type": "string",
        "required": False,
        "description": "Description of the tournament"
      }
    ]

class Tournaments_id:
  url = "/tournaments/TOURNAMENT_ID"

  class Get:
    pass

  class Patch:
    PARAMS = [
      {
        "name": "title",
        "type": "string",
        "required": False,
        "description": "Title of the tournament"
      }, {
        "name": "description",
        "type": "string",
        "required": False,
        "description": "Description of the tournament"
      }
    ]

class Games:
  url = "/games"

  class Get:
    pass

  class Post:
    PARAMS = [
      {
        "name": "tournament_id",
        "type": "id",
        "required": False,
        "description": "ID of the tournament"
      }, {
        "name": "player1_id",
        "type": "id",
        "required": True,
        "description": "ID of the first player"
      }, {
        "name": "player2_id",
        "type": "id",
        "required": True,
        "description": "ID of the second player"
      }, {
        "name": "player1_score",
        "type": "integer",
        "required": True,
        "description": "Score of the first player"
      }, {
        "name": "player2_score",
        "type": "integer",
        "required": True,
        "description": "Score of the second player"
      }
    ]

class Games_id:
  url = "/games/GAME_ID"

  class Get:
    pass

  class Patch:
    PARAMS = [
      {
        "name": "player1_score",
        "type": "integer",
        "required": False,
        "description": "Score of the first player"
      },
      {
        "name": "player2_score",
        "type": "integer",
        "required": False,
        "description": "Score of the second player"
      },
      {
        "name": "status",
        "type": "string",
        "required": False,
        "description": "Status of the game"
      }
    ]

  class Delete:
    pass

class Channels:
  url = "/channels"

  class Get:
    pass

  class Post:
    PARAMS = [
      {
        "name": "name",
        "type": "string",
        "required": True,
        "description": "Name of the channel"
      }
    ]

class Channels_id:
  url = "/channels/CHANNEL_ID"

  class Get:
    pass

  class Patch:
    PARAMS = [
      {
        "name": "name",
        "type": "string",
        "required": False,
        "description": "Name of the channel"
      }
    ]

  class Delete:
    pass

class Channels_id_members:
  url = "/channels/CHANNEL_ID/members"

  class Get:
    pass

  class Patch:
    PARAMS = [
      {
        "name": "user_id",
        "type": "id",
        "required": True,
        "description": "ID of the user to add to the channel"
      }
    ]

class Channels_id_members_id:
  url = "/channels/CHANNEL_ID/members/USER_ID"

  class Delete:
    pass

class Channels_id_messages:
  url = "/channels/CHANNEL_ID/messages"

  class Get:
    pass

  class Post:
    PARAMS = [
      {
        "name": "content",
        "type": "string",
        "required": True,
        "description": "Content of the message"
      }
    ]

class Messages:
  url = "/messages"

  class Get:
    pass

class Messages_id:
  url = "/messages/MESSAGE_ID"

  class Patch:
    PARAMS = [
      {
        "name": "content",
        "type": "string",
        "required": True,
        "description": "Content of the message"
      }
    ]
  
  class Delete:
    pass