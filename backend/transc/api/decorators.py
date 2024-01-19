from . import models
from django.http import JsonResponse
import json
from .models import Channel
from .errors import *

# Not using django.contrib.auth.decorators.login_required because it redirects to /accounts/login/
def login_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
      return JsonResponse({ERROR_FIELD: "Not logged in"}, status=401)
    return view_func(request, *args, **kwargs)
  return wrapped_view

def staff_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_staff:
      return JsonResponse({ERROR_FIELD: "Staff user required"}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view

def superuser_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_staff:
      return JsonResponse({ERROR_FIELD: "Superuser user required"}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view

# Checks for valid JSON syntax of the body and that the specified parameters are existing
def check_body_syntax(parameters=[]):
  def decorator(view_func):
    def wrapped_view(self, request, *args, **kwargs):
      try:
        self.body = json.loads(request.body.decode("utf-8"))
      except:
        return JsonResponse({ERROR_FIELD: "Invalid body JSON syntax"}, status=400)
      for param in parameters:
        if self.body.get(param) is None:
          return JsonResponse({ERROR_FIELD: f"Required body parameter '{param}' missing"}, status=400)
      if len(self.body.keys()) < 1:
        return JsonResponse({ERROR_FIELD: "No parameters specified"}, status=400)
      return view_func(self, request, *args, **kwargs)
    return wrapped_view
  return decorator

def check_object_exists(object_type, id_name, error_string):
  def decorator(view_func):
    def wrapped_view(request, *args, **kwargs):
      try:
        object_type.objects.get(id=kwargs[id_name])
      except:
        return JsonResponse({ERROR_FIELD: error_string}, status=404)
      return view_func(request, *args, **kwargs)
    return wrapped_view
  return decorator

def check_channel_member(view_func):
  def wrapped_view(request, *args, **kwargs):
    try:
      channel = Channel.objects.get(id=kwargs["channel_id"])
    except:
      return JsonResponse({ERROR_FIELD: CHANNEL_404}, status=404)
    if request.user not in channel.members.all():
      return JsonResponse({ERROR_FIELD: CHANNEL_403}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view