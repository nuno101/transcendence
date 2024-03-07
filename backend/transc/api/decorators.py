from . import models
from django.http import JsonResponse
import json
from .models import Channel
from .constants_http_response import *
from .constants_endpoint_structure import ENDPOINTS, BODY_METHODS
from .helpers_decorators import *

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

def check_structure(endpoint_key):
  def decorator(view_func):
    def wrapped_view(request, *args, **kwargs):
      endpoint = ENDPOINTS.get(endpoint_key)
      if endpoint is None:
        return JsonResponse({ERROR_FIELD: "Endpoint documentation missing"}, status=500)
      method = endpoint["methods"].get(request.method)
      if method is None:
        return JsonResponse({ERROR_FIELD: f"Endpoint method {request.method}" +
                                           " documentation missing"}, status=500)

      response = check_query_params(method["query_params"], request.GET)
      if response:
        return response

      if request.json is not None:
        response = check_body_json_params(method["body_params"], request.json)
        if response:
          return response
      elif method.get("content_type") == "application/json":
        return JsonResponse({ERROR_FIELD: f'Invalid request mime type: {request.content_type}' + 
                                           ' -> application/json required'}, status=400)
      return view_func(request, *args, **kwargs)
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
      request.channel = channel
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
      request.message = message
    except:
      return JsonResponse({ERROR_FIELD: MESSAGE_404}, status=404)
    if request.user.id is not message.author.id:
      return JsonResponse({ERROR_FIELD: MESSAGE_403}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view
