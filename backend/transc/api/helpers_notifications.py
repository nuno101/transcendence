from .models import Notification
from . import bridge_websocket as websocket
from .constants_websocket_events import *

def create_notification(type, content, user):
		notification = Notification.objects.create(type=type, content=content, user=user)
		notification.save()

		websocket.send_user_event(user.id, CREATE_NOTIFICATION, notification.serialize())

		return notification

def delete_notification(notification):
		notification_id = notification.id
		notification.delete()

		websocket.send_user_event(notification.user.id, DELETE_NOTIFICATION, {"id": notification_id })

		return notification