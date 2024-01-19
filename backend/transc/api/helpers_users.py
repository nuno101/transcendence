from django.http import JsonResponse
import datetime

def update_user(user, parameters):
  if parameters.get('username') is not None:
    user.username = parameters.get('username')
  # TODO: add option for password change
  user.updated_at = datetime.datetime.now()
  try:
    user.save()
  except:
    return JsonResponse({"reason": "Failed to update user"}, status=400)
  return JsonResponse({'user': user.serialize()}, status=200)