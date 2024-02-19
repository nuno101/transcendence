from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError
import datetime
from .models import Channel
from . import bridge_websocket as websocket
from .constants_http_response import *
from .constants_websocket_events import *

# Channel instance management helpers
def update_channel(channel: Channel, parameters):
  try:
    if parameters.get('name') is not None:
      channel.content = parameters.get('name')
    channel.clean_all()
    channel.save()
  except ValidationError as e:
    return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
  except Exception as e:
    return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)
  
  websocket.send_channel_event(channel.id, UPDATE_CHANNEL, channel.serialize())

  return JsonResponse(channel.serialize())

def delete_channel(channel: Channel):
  channel_id = channel.id
  channel.delete()

  websocket.send_channel_event(channel_id, DELETE_CHANNEL, {"id": channel_id })

  return HttpResponse(status=204)