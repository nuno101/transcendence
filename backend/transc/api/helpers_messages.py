from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError
import datetime
from .models import Channel, Message, User
from . import bridge_websocket as websocket
from .constants_websocket_events import *
from .constants_http_response import *

def update_message(message: Message, parameters):
  try:
    message.content = parameters.get('content')
    message.full_clean()
    message.save()
  except ValidationError as e:
    return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
  except Exception as e:
    return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)

  websocket.send_channel_event(message.channel.id, UPDATE_MESSAGE, message.serialize())
  
  return JsonResponse(message.serialize())

def delete_message(message: Message):
  channel_id = message.channel.id
  message_id = message.id
  message.delete()

  websocket.send_channel_event(channel_id, DELETE_MESSAGE, {"id": message_id })

  return HttpResponse(status=204)