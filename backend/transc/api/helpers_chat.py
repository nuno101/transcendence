from django.http import JsonResponse, HttpResponse
import datetime
from .models import Channel, Message
from . import helpers_websocket as websocket
from .errors import *

# TODO: Implement functions (e.g. add_member_to_channel?, remove_member_from_channel?, etc.)
# This can then be used in multiple places (e.g. views_chat.py, views_personal.py, etc.)
# This also allows for easier implementation of websocket notifications since there is only one function that performs one action

def create_message(channel: Channel, user, parameters):
  message = Message(channel=channel, author=user, content=parameters.get('content'))
  try:
    message.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to create message"}, status=500)

  websocket.send_channel_notification(channel.id, { # TODO: Test websocket notification system
    "event": "create_message",
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
    "event": "update_message",
    "data": {
      "message": message.serialize()
    }
  })
  return JsonResponse({'message': message.serialize()}, status=200)

def delete_message(message: Message):
  message.delete() # TODO: Test if deleting before getting the id is a problem

  websocket.send_channel_notification(message.channel.id, { # TODO: Test websocket notification system
    "event": "delete_message",
    "data": {
      "message_id": message.id
    }
  })
  return HttpResponse(status=204)