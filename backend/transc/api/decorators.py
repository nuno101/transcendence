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

def staff_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_staff:
      return JsonResponse({"reason": "Staff user required"}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view

def superuser_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_staff:
      return JsonResponse({"reason": "Superuser user required"}, status=403)
    return view_func(request, *args, **kwargs)
  return wrapped_view

# Checks for valid JSON syntax of the body and that the specified parameters are existing
def check_body_syntax(parameters=[]):
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

def check_object_exists(object_type, id_name, error_string):
  def decorator(view_func):
    def wrapped_view(request, *args, **kwargs):
      try:
        object_type.objects.get(id=kwargs[id_name])
      except:
        return JsonResponse({"reason": error_string}, status=404)
      return view_func(request, *args, **kwargs)
    return wrapped_view
  return decorator