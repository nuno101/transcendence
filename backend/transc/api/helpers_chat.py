from django.http import JsonResponse, HttpResponse
import datetime
from .models import Message
from .errors import *

def create_message(channel, user, parameters):
  message = Message(channel=channel, user=user, content=parameters.get('content'))
  message.save()
  # send_to_group(f"chat_{id}", { # TODO: Implement websocket functionality
  #   "event": "new_message",
  #   "data": {
  #     "message": message.serialize()
  #   }
  # })
  return JsonResponse({'message': message.serialize()}, status=201)

def update_message(message, parameters):
  if parameters.get('content') is not None:
    message.content = parameters.get('content')
  message.updated_at = datetime.datetime.now()
  try:
    message.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update message"}, status=400)
  return JsonResponse({'message': message.serialize()}, status=200)

def delete_message(message):
  message.delete()
  # send_to_group(f"chat_{id}", { # TODO: Implement websocket functionality
  #   "event": "delete_message",
  #   "data": {
  #     "message_id": mid
  #   }
  # })
  return HttpResponse(status=204)