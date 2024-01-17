from . import models
from django.http import JsonResponse

# Not using django.contrib.auth.decorators.login_required because it redirects to /accounts/login/
def login_required(view_func):
  def wrapped_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
      return JsonResponse({"reason": "Not logged in"}, status=401)
    return view_func(request, *args, **kwargs)
  return wrapped_view

def check_tournament_exists(view_func):
  def wrapped_view(request, *args, **kwargs):
    try:
      models.Tournament.objects.get(id=kwargs["tournament_id"])
    except:
      return JsonResponse({"reason": "Tournament does not exist"}, status=404)
    return view_func(request, *args, **kwargs)
  return wrapped_view