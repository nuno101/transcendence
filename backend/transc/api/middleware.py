from django.http import JsonResponse
from .constants_endpoint_structure import ENDPOINTS
from .constants_http_response import ERROR_FIELD
import json

# cCONF: Endpoints access allowed for anonymous users
ANONYMOUS_ACCESS = {
	"/login": ["POST"],
	"/users": ["POST"],
}

class LoggedInCheckMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		# TODO: Maybe find way to check for this not hardcoded
		# Allow if path starts with /admin
		if request.path.startswith("/admin"):
			return self.get_response(request)

		# Check if endpoint is allowed for anonymous users
		# return JsonResponse({"test": request.resolver_match})
		if request.path in ANONYMOUS_ACCESS.keys():
			if request.method in ANONYMOUS_ACCESS[request.path]:
				return self.get_response(request)

		# # Check if user is logged in
		if not request.user.is_authenticated:
			return JsonResponse({ERROR_FIELD: "Not logged in"}, status=401)

		return self.get_response(request)

# cCONF: Methods that require a body
METHODS_WITH_BODY = ["POST", "PATCH"]

class JsonSyntaxCheckMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if request.method in METHODS_WITH_BODY and request.content_type == "application/json":
			try:
				request.json = json.loads(request.body.decode("utf-8"))
			except:
				return JsonResponse({ERROR_FIELD: "Invalid JSON"}, status=400)
		else:
			request.json = None
		return self.get_response(request)

# TODO: Fix and enable or remove
# Problems are: admin panel not working without hardcoded temporary fix
# request.endpoint_key not found for many error responses handled by django instead of the api
class ResponseCodeCheckMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)

		# TODO: Maybe find way to check for this not hardcoded
		# Return if path starts with /admin since it is not part of the API structure defined
		if request.path.startswith("/admin"):
			return response

		# endpoint = ENDPOINTS.get(request.endpoint_key)
		# method = endpoint["methods"].get(request.method)

		# TODO: Enable once responses have been documented for all endpoints
		# Figure out if there is an easier way to do document all responses

		# Check response code
		# responses = method.get("responses")
		# if not responses or str(response.status_code) not in responses.keys():
		# 	code = response.status_code
		# 	return JsonResponse({ERROR_FIELD: "Endpoint method response documentation" +
		# 									 f" missing for code {code}"},status=500)
		return response