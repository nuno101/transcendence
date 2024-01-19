from django.http import JsonResponse, HttpResponse
import datetime
from .models import Channel, Message
from .errors import *

def create_message(channel: Channel, user, parameters):
  message = Message(channel=channel, author=user, content=parameters.get('content'))
  message.save()
  # send_to_group(f"chat_{id}", { # TODO: Implement websocket functionality
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
  return JsonResponse({'message': message.serialize()}, status=200)

def delete_message(message: Message):
  message.delete()
  # send_to_group(f"chat_{id}", { # TODO: Implement websocket functionality
  #   "event": "delete_message",
  #   "data": {
  #     "message_id": mid
  #   }
  # })
  return HttpResponse(status=204)