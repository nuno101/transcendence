from . import models
from django.http import JsonResponse
import json
from .models import Channel
from .constants_http_response import *
from .constants_endpoint_structure import ENDPOINTS, BODY_METHODS

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

      # Check query parameters
      query_params = method["query_params"]
      in_query_params = list(request.GET.keys())
      for param in query_params:
        exists = request.GET.get(param) is not None
        if not exists and query_params[param]["required"]:
          return JsonResponse({ERROR_FIELD: "Missing required query " +
                                           f"parameter: {param}"}, status=400)
        if exists:
          in_query_params.remove(param)

      if len(in_query_params) > 0:
        return JsonResponse({ERROR_FIELD: f"Unknown query parameter(s): " +
                                          f"{in_query_params}"}, status=400)
      
      # Check body parameters
      if request.json is not None:
        body_params = method["body_params"]
        in_body_params = list(request.json.keys())
        for param in body_params:
          exists = param in request.json
          if not exists and body_params[param]["required"]:
            return JsonResponse({ERROR_FIELD: "Missing required body " +
                                             f"parameter: {param}"}, status=400)
          if exists:
            in_body_params.remove(param)

        if len(in_body_params) > 0:
          return JsonResponse({ERROR_FIELD: "Unknown body parameter(s):" +
                                           f" {in_body_params}"}, status=400)
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
