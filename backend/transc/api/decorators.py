from . import models
from django.http import JsonResponse
import json

# Not using django.contrib.auth.decorators.login_required because it redirects to /accounts/login/
def login_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
      return JsonResponse({"reason": "Not logged in"}, status=401)
    return view_func(request, *args, **kwargs)
  return wrapped_view

# Checks for valid JSON syntax of the body and that the specified parameters are existing
def check_body_syntax(parameters):
  def decorator(view_func):
    def wrapped_view(self, request, *args, **kwargs):
      try:
        self.body = json.loads(request.body.decode("utf-8"))
      except:
        return JsonResponse({"reason": "Invalid body JSON syntax"}, status=400)
      for param in parameters:
        if self.body.get(param) is None:
          return JsonResponse({"reason": f"Required body parameter '{param}' missing"}, status=400)
      return view_func(self, request, *args, **kwargs)
    return wrapped_view
  return decorator


def check_tournament_exists(view_func):
  def wrapped_view(request, *args, **kwargs):
    try:
      models.Tournament.objects.get(id=kwargs["tournament_id"])
    except:
      return JsonResponse({"reason": "Tournament does not exist"}, status=404)
    return view_func(request, *args, **kwargs)
  return wrapped_view

def check_game_exists(view_func):
  def wrapped_view(request, *args, **kwargs):
    try:
      models.Game.objects.get(id=kwargs["game_id"])
    except:
      return JsonResponse({"reason": "Game does not exist"}, status=404)
    return view_func(request, *args, **kwargs)
  return wrapped_view
