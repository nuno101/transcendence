from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Description: Helper functions to make it easier to send messages 
# to websocket consumer groups and users.

def message_group(group, type, event):
  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.group_send)(group, {
    "type": type,
    "data": event
  })

def send_user_notification(user_id, event):
  message_group(f"user_{user_id}", "send_notification", event)

def send_channel_notification(channel_id, event):
  message_group(f"channel_{channel_id}", "send_notification", event)

def add_consumer_to_group(user_id, target_group):
  message_group(f'user_{user_id}', 'add_group', {
    'group': target_group
  })

def remove_consumer_from_group(user_id, target_group):
  message_group(f'user_{user_id}', 'remove_group', {
    'group': target_group
  })