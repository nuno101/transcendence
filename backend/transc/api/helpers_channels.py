from django.http import JsonResponse
import datetime
from .models import Channel
from .errors import *

def update_channel(channel: Channel, parameters):
  if parameters.get('name') is not None:
    channel.content = parameters.get('name')
  channel.updated_at = datetime.datetime.now()
  try:
    channel.save()
  except:
    return JsonResponse({ERROR_FIELD: "Failed to update channel"}, status=500)
  
  # TODO: Implement websocket notification

  return JsonResponse({'channel': channel.serialize()}, status=200)