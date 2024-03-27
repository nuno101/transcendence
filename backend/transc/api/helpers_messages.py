from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ValidationError
import datetime
from .models import Channel, Message, User
from . import bridge_websocket as websocket
from .constants_websocket_events import *
from .constants_http_response import *

def delete_message(message: Message):
  channel_id = message.channel.id
  message_id = message.id
  message.delete()

  websocket.send_channel_event(channel_id, DELETE_MESSAGE, {"id": message_id })

  return HttpResponse(status=204)