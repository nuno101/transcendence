import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.models import Channel
from asgiref.sync import sync_to_async
from . import handler_consumers as handlers
from api.helpers_users import update_user_status

class Consumer(AsyncWebsocketConsumer):
    # Connection methods

    async def connect(self):
        self.groups = []
        self.user_id = None

        user = self.scope.get('user')
        if user.is_anonymous:
            await self.accept()
            await self.send_error('Not logged in')
            await self.close()
            return 
        self.user_id = user.id

        # Add consumer default notification groups
        await self._add_group(f'user_{self.user_id}')
        user_channels = await sync_to_async(list)(Channel.objects.filter(members=user))
        for channel in user_channels:
            await self._add_group(f'channel_{channel.id}')
        
        # Add consumer to friends status groups
        user_friends = await sync_to_async(list)(user.friends.all())
        for friend in user_friends:
            await self._add_group(f'user_status_{friend.id}')

        # Check if consumer is the first of its user by checking status
        await self._add_group(f'user_status_{user.id}')
        await sync_to_async(update_user_status)(user, 'online')

        await self.accept()

    async def disconnect(self, close_code):
        if not self.user_id:
            return

        for group in self.groups:
            await self._remove_group(group)

        user = await sync_to_async(User.objects.get)(id=self.user_id)
        await sync_to_async(update_user_status)(user, 'offline')

    # Client event handling method
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            event = data['event']
            payload = data['payload']
        except:
            await self.send_error('Invalid data format')
            return
        case = next((x for x in handlers.VALID_CLIENT_EVENTS if event in x), None)
        if case is None:
            await self.send_error('Invalid event')
        else:
            await getattr(handlers, case[event])(self, payload)

    # Group event handling methods
    async def close_connection(self, event):
        await self.close()

    async def send_event(self, event):
        data = self.get_field(event, 'data')
        if data is not None:
            await self.send(text_data=json.dumps(data))

    async def add_group(self, event):
        data = self.get_field(event, 'data')
        if data is not None:
            await self._add_group(data['group'])

    async def remove_group(self, event):
        data = self.get_field(event, 'data')
        if data is not None:
            await self._remove_group(data['group'])

    # Helper methods
    def get_field(self, data, field):
        if field in data:
            return data[field]
        self.send_error("Internal server error")
        return None

    async def send_error(self, message):
        await self.send(text_data=json.dumps({
            'event': 'error',
            'payload': {
                'message': message
            }
        }))

    async def _add_group(self, group):
        await self.channel_layer.group_add(
            group,
            self.channel_name
        )
        self.groups.append(group)

    async def _remove_group(self, group):
        await self.channel_layer.group_discard(
            group,
            self.channel_name
        )
        self.groups.remove(group)
