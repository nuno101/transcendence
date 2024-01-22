from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Description: Helper functions to make it easier to implement
#              websocket notifications for http requests

def message_group(group, type, data):
  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.group_send)(group, {
    "type": type,
    "data": data
  })

def send_user_notification(user_id, event, payload):
  message_group(f"user_{user_id}", "send_notification", {
    "event": event,
    "payload": payload
  })

def send_user_status_notification(user_id, event, payload):
  message_group(f"user_status_{user_id}", "send_notification", {
    "event": event,
    "payload": payload
  })

def send_channel_notification(channel_id, event, payload):
  message_group(f"channel_{channel_id}", "send_notification", {
    "event": event,
    "payload": payload
  })

def add_consumer_to_group(user_id, target_group):
  message_group(f'user_{user_id}', 'add_group', {
    'group': target_group
  })

def remove_consumer_from_group(user_id, target_group):
  message_group(f'user_{user_id}', 'remove_group', {
    'group': target_group
  })