# cCONF: Constants for outgoing websocket events (server -> client)

# User events
UPDATE_USER = "update_user" # Expected payload: SERIALIZED_USER
DELETE_USER = "delete_user" # Expected payload: { "id": USER_ID }

# Notification events
CREATE_NOTIFICATION = "create_notification" # Expected payload: SERIALIZED_NOTIFICATION
DELETE_NOTIFICATION = "delete_notification" # Expected payload: { "id": NOTIFICATION_ID }

# Friend events
REMOVE_FRIEND = "remove_friend" # Expected payload: { "id": USER_ID }

# Friend request events
CREATE_FRIEND_REQUEST = "create_friend_request" # Expected payload: SERIALIZED_FRIEND_REQUEST
ACCEPT_FRIEND_REQUEST = "accept_friend_request" # Expected payload: SERIALIZED_FRIEND_REQUEST
CANCEL_FRIEND_REQUEST = "cancel_friend_request" # Expected payload: { "id": FRIEND_REQUEST_ID }
DECLINE_FRIEND_REQUEST = "decline_friend_request" # Expected payload: { "id": FRIEND_REQUEST_ID }

# Tournament/Game events
TOURNAMENT_STARTING = "tournament_starting" # Expected payload: { "id": TOURNAMENT_ID}

# Message events
CREATE_MESSAGE = "create_message" # Expected payload: SERIALIZED_MESSAGE
UPDATE_MESSAGE = "update_message" # Expected payload: SERIALIZED_MESSAGE
DELETE_MESSAGE = "delete_message" # Expected payload: { "id": MESSAGE_ID }

# Channel events
CREATE_CHANNEL = "create_channel" # Expected payload: SERIALIZED_CHANNEL
UPDATE_CHANNEL = "update_channel" # Expected payload: SERIALIZED_CHANNEL
DELETE_CHANNEL = "delete_channel" # Expected payload: { "id": CHANNEL_ID }