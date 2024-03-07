from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.utils.decorators import method_decorator
from . import bridge_websocket as websocket
from .decorators import *
from .constants_http_response import *
#from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
	logger.debug("Hello world from the custom debug log")
	return JsonResponse({'response': "Hello, world. You're at the transcendence index."})

def test_websocket(request): # FIXME: DEBUG: Remove later
	return render(request, 'api/custom_ws.html')

# Endpoint: /login
@method_decorator(check_structure("/login"), name='dispatch')
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
@method_decorator(check_structure("/logout"), name='dispatch')
class Logout(View):
	def post(self, request):
		websocket.message_group(f'user_{request.user.id}', 'close_connection', {})
		logout(request)

		return JsonResponse({'response': "Successfully logged out"})

# TODO - test: Endpoint: /authenticate
@method_decorator(check_structure("/authenticate"), name='dispatch')
class Authenticate(View):
	def post(self, request):
		user = authenticate(username=request.json.get('username'), password=request.json.get('password'))
		if isinstance(user, User):
			return JsonResponse(user.serialize())
		else:
			return JsonResponse({ERROR_FIELD: "Not authenticated"}, status=401)
