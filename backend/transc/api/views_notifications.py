from django.views import View
from django.utils.decorators import method_decorator
from .decorators import *
from django.http import JsonResponse, HttpResponse
from .models import Notification
from .helpers_notifications import *
from .constants_http_response import *

# Endpoint: /users/me/notifications
@method_decorator(login_required, name='dispatch')
class NotificationCollection(View):
	def get(self, request):
		notifications = request.user.notifications.all()
		return JsonResponse([n.serialize() for n in notifications], safe=False)

# Endpoint: /users/me/notifications/<int:notification_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Notification, 'notification_id', NOTIFICATION_404), name='dispatch')
class NotificationSingle(View):
	def delete(self, request, notification_id):
		notification = Notification.objects.get(pk=notification_id)

		# Check if user owns notification
		if notification.user.id != request.user.id:
			return JsonResponse({ERROR_FIELD: NOTIFICATION_403}, status=400)
		delete_notification(notification)
		return HttpResponse(status=204)