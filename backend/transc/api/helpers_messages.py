from django.http import JsonResponse, HttpResponse
import datetime
from .models import Channel, Message, User
from . import bridge_websocket as websocket
from .constants_websocket_events import *
from .constants_http_response import *

# Message instance management helpers
def create_message(channel: Channel, user: User, parameters):
  try:
    message = Message.objects.create(channel=channel, author=user, 
                                     content=parameters.get('content'))
  except:
    return JsonResponse({ERROR_FIELD: "Failed to create message"}, status=500)

  websocket.send_channel_event(channel.id, CREATE_MESSAGE, message.serialize())
  return JsonResponse(message.serialize(), status=201)

def update_message(message: Message, parameters):
  if parameters.get('content') is not None:
    message.content = parameters.get('content')
  message.updated_at = datetime.datetime.now()
  try:
    message.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update message"}, status=500)

  websocket.send_channel_event(message.channel.id, UPDATE_MESSAGE, message.serialize())
  return JsonResponse(message.serialize())

def delete_message(message: Message):
  channel_id = message.channel.id
  message_id = message.id
  message.delete()

  websocket.send_channel_event(channel_id, DELETE_MESSAGE, {"id": message_id })
  return HttpResponse(status=204)