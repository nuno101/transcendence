from django.http import JsonResponse, HttpResponse
import datetime
from .models import Channel, Message
from .errors import *

# TODO: Implement functions (e.g. add_member_to_channel, remove_member_from_channel, etc.)
# This can then be used in multiple places (e.g. views_chat.py, views_personal.py, etc.)
# This also allows for easier implementation of websocket notifications since there is only one function that performs one action

# TODO: Figure out how to implement websocket notifications -> How to design the websocket notification system?

def create_message(channel: Channel, user, parameters):
  message = Message(channel=channel, author=user, content=parameters.get('content'))
  message.save()
  # send_to_group(f"chat_{id}", { # TODO: Implement websocket notification
  #   "event": "new_message",
  #   "data": {
  #     "message": message.serialize()
  #   }
  # })
  return JsonResponse({'message': message.serialize()}, status=201)

def update_message(message: Message, parameters):
  if parameters.get('content') is not None:
    message.content = parameters.get('content')
  message.updated_at = datetime.datetime.now()
  try:
    message.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update message"}, status=500)
  
  # TODO: Implement websocket notification

  return JsonResponse({'message': message.serialize()}, status=200)

def delete_message(message: Message):
  message.delete()
  # send_to_group(f"chat_{id}", { # TODO: Implement websocket notification
  #   "event": "delete_message",
  #   "data": {
  #     "message_id": mid
  #   }
  # })
  return HttpResponse(status=204)