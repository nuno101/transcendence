from django.http import JsonResponse
import datetime
from .models import Channel
from . import helpers_websocket as websocket
from .errors import *

def update_channel(channel: Channel, parameters):
  if parameters.get('name') is not None:
    channel.content = parameters.get('name')
  channel.updated_at = datetime.datetime.now()
  try:
    channel.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update channel"}, status=500)
  
  websocket.send_channel_notification(channel.id, { # TODO: Test websocket notification system
    "event": "update_channel",
    "data": {
      "channel": channel.serialize()
    }
  })
  return JsonResponse({'channel': channel.serialize()}, status=200)