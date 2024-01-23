from django.http import JsonResponse, HttpResponse
import datetime
from .models import Channel
from . import bridge_websocket as websocket
from .constants_http_response import *
from .constants_websocket_events import *

def update_channel(channel: Channel, parameters):
  if parameters.get('name') is not None:
    channel.content = parameters.get('name')
  channel.updated_at = datetime.datetime.now()
  try:
    channel.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update channel"}, status=500)
  
  websocket.send_channel_notification(channel.id, UPDATE_CHANNEL, channel.serialize())
  return JsonResponse(channel.serialize())

def delete_channel(channel: Channel):
  channel_id = channel.id
  channel.delete()

  websocket.send_channel_notification(channel_id, DELETE_CHANNEL, {
    "channel_id": channel_id })
  return HttpResponse(status=204)