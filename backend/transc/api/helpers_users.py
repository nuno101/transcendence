from django.http import JsonResponse, HttpResponse
import datetime
from .models import User
from . import helpers_websocket as websocket
from .constants_errors import *

def update_user(user: User, parameters: dict):
  if parameters.get('username') is not None:
    user.username = parameters.get('username')
  if parameters.get('password') is not None:
    user.set_password(parameters.get('password'))
  user.updated_at = datetime.datetime.now()
  try:
    user.save()
  except Exception as e:
    if 'duplicate key' in str(e):
      return JsonResponse({ERROR_FIELD: "Username already taken"}, status=400)
    else:
      return JsonResponse({ERROR_FIELD: "Undefined error"}, status=500)
  
  # TODO: Figure out how to do group notifications for this type of event
  # will also be usefull for imeplementation of the online status feature
  # websocket.send_user_notification(user.id, {
  #   "event": UPDATE_USER,
  #   "data": {
  #     "user": user.serialize()
  #   }
  # })
  return JsonResponse({'user': user.serialize()}, status=200)

def delete_user(user: User):
  # user_id = user.id
  user.delete()

  # TODO: Figure out how to do group notifications for this type of event
  # will also be usefull for imeplementation of the online status feature
  # websocket.send_user_notification(user_id, {
  #   "event": DELETE_USER,
  #   "data": {
  #     "user_id": user_id
  #   }
  # })
  return HttpResponse(status=204)