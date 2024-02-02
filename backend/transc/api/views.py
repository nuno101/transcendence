from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from . import bridge_websocket as websocket
from .decorators import *
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import render

def index(request):
	return JsonResponse({'response': "Hello, world. You're at the transcendence index."})

def websocket_custom(request): # FIXME: DEBUG: Remove later
	return render(request, 'api/custom_ws.html')

# Endpoint: /login
class Login(View):
	def post(self, request):
		user = authenticate(username=request.json.get('username'), 
												password=request.json.get('password'))
		if user is None:
			return JsonResponse({ERROR_FIELD: "Invalid login credentials"}, status=401)
		expiration = None if request.GET.get('remember', "false") == 'true' else 0
		request.session.set_expiry(expiration)
		login(request, user)
		return JsonResponse(user.serialize(private=True))

# Endpoint: /logout
class Logout(View):
	def post(self, request):
		websocket.message_group(f'user_{request.user.id}', 'close_connection', {})
		logout(request)
		return JsonResponse({'response': "Successfully logged out"})