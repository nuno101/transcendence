from django.http import JsonResponse, HttpResponse
import datetime
from .models import Channel, Message
from . import helpers_websocket as websocket
from .constants_ws_notification import *
from .constants_errors import *

# TODO: Implement functions (e.g. add_member_to_channel?, remove_member_from_channel?, etc.)
# This can then be used in multiple places (e.g. views_chat.py, views_personal.py, etc.)
# This also allows for easier implementation of websocket notifications since there is only one function that performs one action

# TODO: Maybe find way or alternative to datetime which can be better serialized to JSON or something else?

def create_message(channel: Channel, user, parameters):
  message = Message(channel=channel, author=user, content=parameters.get('content'))
  try:
    message.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to create message"}, status=500)

  websocket.send_channel_notification(channel.id, { # TODO: Test websocket notification system
    "event": CREATE_MESSAGE,
    "data": {
      "message": message.serialize()
    }
  })
  return JsonResponse({'message': message.serialize()}, status=201)

def update_message(message: Message, parameters):
  if parameters.get('content') is not None:
    message.content = parameters.get('content')
  message.updated_at = datetime.datetime.now()
  try:
    message.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update message"}, status=500)

  websocket.send_channel_notification(message.channel.id, { # TODO: Test websocket notification system
    "event": UPDATE_MESSAGE,
    "data": {
      "message": message.serialize()
    }
  })
  return JsonResponse({'message': message.serialize()}, status=200)

def delete_message(message: Message):
  channel_id = message.channel.id
  message_id = message.id
  message.delete()

  websocket.send_channel_notification(channel_id, { # TODO: Test websocket notification system
    "event": DELETE_MESSAGE,
    "data": {
      "message_id": message_id
    }
  })
  return HttpResponse(status=204)