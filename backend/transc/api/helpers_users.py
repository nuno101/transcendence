from django.http import JsonResponse
import datetime
from .errors import *

def update_user(user, parameters: dict):
  if parameters.get('username') is not None:
    user.username = parameters.get('username')
  # TODO: add option for password change
  user.updated_at = datetime.datetime.now()
  try:
    user.save()
  except Exception as e:
    if 'duplicate key' in str(e):
      return JsonResponse({ERROR_FIELD: "Username already taken"}, status=400)
    else:
      return JsonResponse({ERROR_FIELD: "Undefined error"}, status=400)
  return JsonResponse({'user': user.serialize()}, status=200)