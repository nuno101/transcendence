from .models import Notification
from . import bridge_websocket as websocket
from .constants_websocket_events import *

def delete_notification(notification):
		notification_id = notification.id
		notification.delete()

		websocket.send_user_event(notification.user.id, DELETE_NOTIFICATION, {"id": notification_id })

		return notification