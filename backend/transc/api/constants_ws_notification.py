# Description: Notification websocket constants

# User events
USER_STATUS_UPDATE = "user_status_update" # TODO: Implement user events like online status, etc.
UPDATE_USER = "update_user"
DELETE_USER = "delete_user"

# Friend events
ADD_FRIEND = "add_friend"
REMOVE_FRIEND = "remove_friend"

# Friend request events
SEND_FRIEND_REQUEST = "send_friend_request"
ACCEPT_FRIEND_REQUEST = "accept_friend_request"
CANCEL_FRIEND_REQUEST = "cancel_friend_request"
DECLINE_FRIEND_REQUEST = "decline_friend_request"

# Message events
CREATE_MESSAGE = "create_message"
UPDATE_MESSAGE = "update_message"
DELETE_MESSAGE = "delete_message"

# Channel events
CREATE_CHANNEL = "create_channel"
UPDATE_CHANNEL = "update_channel"
DELETE_CHANNEL = "delete_channel"

# Member events
ADD_CHANNEL_MEMBER = "add_channel_member"
REMOVE_CHANNEL_MEMBER = "remove_channel_member"