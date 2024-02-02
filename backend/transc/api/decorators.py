from . import models
from django.http import JsonResponse
import json
from .models import Channel
from .constants_http_response import *
from .constants_endpoint_structure import *

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

BODY_REQUEST_METHODS = ["POST", "PATCH", "PUT"]

def validate_body_parameters(self, request, url):
  # Check for existing parameters
  input_keys = list(self.body.keys())
  params = get_body_params(url, request.method)
  for param_key in params.keys():
    if params[param_key]["required"] and param_key not in input_keys:
      return JsonResponse({ERROR_FIELD: f"Missing required parameter '{param_key}'"}, status=400)
    if param_key in input_keys:
      input_keys.remove(param_key)

  if len(input_keys) > 0:
    return JsonResponse({ERROR_FIELD: f"Unknown parameter(s) '{', '.join(input_keys)}'"}, status=400)
  
  return None

# Checks for valid JSON syntax of the body and that the specified parameters are existing
def check_structure(endpoint_url):
  def decorator(view_func):
    def wrapped_view(self, request, *args, **kwargs):
      if request.method in BODY_REQUEST_METHODS:
        # Check for valid JSON syntax
        try:
          self.body = json.loads(request.body.decode("utf-8"))
        except:
          return JsonResponse({ERROR_FIELD: "Invalid body JSON syntax"}, status=400)

        check = validate_body_parameters(self, request, endpoint_url)
        if check is not None:
          return check
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

def check_message_author(view_func):
  def wrapped_view(request, *args, **kwargs):
    try:
      message = models.Message.objects.get(id=kwargs["message_id"])
    except:
      return JsonResponse({ERROR_FIELD: MESSAGE_404}, status=404)
    if request.user.id is not message.author.id:
      return JsonResponse({ERROR_FIELD: MESSAGE_403}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view
