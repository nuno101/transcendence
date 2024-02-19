from django.views import View
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from .decorators import *
from django.http import JsonResponse, HttpResponse
from .models import Notification
from .helpers_notifications import *
from .constants_http_response import *

# Endpoint: /users/me/notifications
@method_decorator(check_structure("/users/me/notifications"), name='dispatch')
class NotificationCollection(View):
	def get(self, request):
		notifications = request.user.notifications.all()
		return JsonResponse([n.serialize() for n in notifications], safe=False)
	
	def post(self, request):
		type = request.json.get('type')
		content = request.json.get('content')
		try:
			notification = Notification(type=type, content=content, user=request.user)
			notification.full_clean()
			notification.save()
		except ValidationError as e:
			return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
		except Exception as e:
			return JsonResponse({ERROR_FIELD: str(e)}, status=500)

		return JsonResponse(notification.serialize(), status=201)

# Endpoint: /users/me/notifications/NOTIFICATION_ID
@method_decorator(check_structure("/users/me/notifications/NOTIFICATION_ID"), name='dispatch')
@method_decorator(check_object_exists(Notification, 'notification_id', NOTIFICATION_404), name='dispatch')
class NotificationSingle(View):
	def delete(self, request, notification_id):
		notification = Notification.objects.get(id=notification_id)

		# Check if user owns notification
		if notification.user.id != request.user.id:
			return JsonResponse({ERROR_FIELD: NOTIFICATION_403}, status=400)

		delete_notification(notification)
		return HttpResponse(status=204)