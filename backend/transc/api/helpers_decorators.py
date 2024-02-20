from django.http import JsonResponse
from .constants_http_response import *

def check_query_params(query_structure, query_input):
  in_keys = list(query_input.keys())
  for param in query_structure:
    in_param = query_input.get(param) is not None
    if not in_param and query_structure[param]["required"]:
      return JsonResponse({ERROR_FIELD: "Missing required query " +
                                         f"parameter: {param}"}, status=400)
    if in_param:
      in_keys.remove(param)

  if len(in_keys) > 0:
    return JsonResponse({ERROR_FIELD: f"Unknown query parameter(s): " +
                                      f"{in_keys}"}, status=400)

  return None

def check_body_json_params(body_structure, body_input):
  in_keys = list(body_input.keys())
  for param in body_structure:
    in_param = param in body_input
    if not in_param and body_structure[param]["required"]:
      return JsonResponse({ERROR_FIELD: "Missing required body " +
                                        f"parameter: {param}"}, status=400)
    if in_param:
      in_keys.remove(param)

  if len(in_keys) > 0:
    return JsonResponse({ERROR_FIELD: "Unknown body parameter(s):" +
                                      f" {in_keys}"}, status=400)

  return None