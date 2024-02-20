from django.http import JsonResponse, HttpResponse
import datetime
from .models import User
from . import bridge_websocket as websocket
from .constants_http_response import *
from .constants_websocket_events import *
from .models import Tournament

# User instance management helpers
def update_user(user: User, parameters: dict):
  try:
    if parameters.get('nickname') is not None:
      user.nickname = parameters.get('nickname')
    if parameters.get('password') is not None:
      user.set_password(parameters.get('password'))
    test = parameters.get('tournament_id')
    if test is not None:
      try:
        tournament = Tournament.objects.get(id=test)
        user.tournaments.add(tournament)
      except Tournament.DoesNotExist:
        print(f"Tournament with ID {test} does not exist.")
    user.save()

  except Exception as e:
    if 'duplicate key' and 'nickname' in str(e):
      return JsonResponse({ERROR_FIELD: "Nickname already taken"}, status=400)
    else:
      return JsonResponse({ERROR_FIELD: "Internal server error"}, status=500)
  
  # TODO: Implement websocket notification?

  return JsonResponse(user.serialize())

def update_user_status(user, status):
  user.status = status
  user.save()
  websocket.send_user_status_event(
    user.id, UPDATE_USER, user.serialize(private=True))

def delete_user(user: User):
  # user_id = user.id
  user.delete()

  # TODO: Implement websocket notification?

  return HttpResponse(status=204)