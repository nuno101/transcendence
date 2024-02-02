from django.http import JsonResponse
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
        # Check if endpoint is allowed for anonymous users
        # return JsonResponse({"test": request.resolver_match})
        if request.path in ANONYMOUS_ACCESS.keys():
            if request.method in ANONYMOUS_ACCESS[request.path]:
                return self.get_response(request)

        # Check if user is logged in
        if not request.user.is_authenticated:
            return JsonResponse({ERROR_FIELD: "Not logged in"}, status=401)


        return self.get_response(request)

# cCONF: Methods that require a body
METHODS_WITH_BODY = ["POST", "PATCH"]

class ParameterCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # TODO: Check for required query parameters
        if request.method in METHODS_WITH_BODY:
            if request.content_type == "application/json":
                try:
                    request.json = json.loads(request.body.decode("utf-8"))
                except:
                    return JsonResponse({ERROR_FIELD: "Invalid JSON"}, status=400)
            # TODO: Check for required body parameters
        return self.get_response(request)

class ResponseCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # TODO: Check if response is valid according to endpoint structure
        # If not throw exception and return 500 with explanation that response is not documented correctly