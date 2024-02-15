from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Description: Helper functions to make it easier to send
#              websocket group messages from anywhere

def message_group(group, type, data):
  channel_layer = get_channel_layer()
  async_to_sync(channel_layer.group_send)(group, {
    "type": type,
    "data": data
  })

# Send websocket event to user specific group
def send_user_event(user_id, event, payload):
  message_group(f"user_{user_id}", "send_event", {
    "event": event,
    "payload": payload
  })

# Send status update to user specific group
def send_user_status_event(user_id, event, payload):
  message_group(f"user_status_{user_id}", "send_event", {
    "event": event,
    "payload": payload
  })

# Send websocket event to channel specific group
def send_channel_event(channel_id, event, payload):
  message_group(f"channel_{channel_id}", "send_event", {
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