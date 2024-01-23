from asgiref.sync import sync_to_async
from api.models import User
import json

# cCONF: Constants for client events
# Format "event": "handler"
VALID_CLIENT_EVENTS = [
  {"ping": "ping"},
  # {"subscribe_user_status": "subscribe_user_status"},
  # {"unsubscribe_user_status": "unsubscribe_user_status"},
]

async def ping(self, data):
  await self.send(text_data='{"event": "pong", "payload": {}}')

# TODO: Enable again if it is needed in the future, if it is not needed in the end -> remove
# async def subscribe_user_status(consumer, data):
#   user_ids = data.get('user_ids', None)
#   if user_ids is None:
#     await consumer.send_error('Missing user_ids parameter')
#     return
  
#   subscribed_users = []
#   for user_id in user_ids:
#     # Check if user exists, is not current user and calling is a friend
#     try:
#       user = await sync_to_async(User.objects.get)(id=user_id)
#     except:
#       continue
#     if user == consumer.user or not await sync_to_async(consumer.user.is_friend)(user):
#       continue

#     # Add consumer to user specific group
#     await consumer._add_group(f'user_status_{user.id}')
#     subscribed_users.append(user)

#   await consumer.send(text_data=json.dumps({ # TODO: Implement user status and return right data here
#     "event": "subscribed_user_status",
#     "data": {
#       "user_states": [user.serialize() for user in subscribed_users]
#     }
#     }))

# async def unsubscribe_user_status(consumer, data):
#   user_ids = data.get('user_ids', None)
#   if user_ids is None:
#     await consumer.send_error('Missing user_ids parameter')
#     return

#   for user_id in user_ids:
#     await consumer._remove_group(f'user_status_{user_id}')