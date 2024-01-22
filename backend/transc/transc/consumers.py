import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.models import Channel
from asgiref.sync import sync_to_async

class Consumer(AsyncWebsocketConsumer):
    # Connection methods

    async def connect(self):
        self.user = self.scope.get('user')
        if self.user.is_anonymous:
            await self.close()

        # Add consumer to user specific group
        await self._add_group(f'user_{self.user.id}')

        # Add consumer to channel specific groups
        user_channels = await sync_to_async(self.get_user_channels)()
        for channel in user_channels:
            await self._remove_group(f'channel_{channel.id}')

        await self.accept()

    async def disconnect(self, close_code):
        if self.user.is_anonymous:
            return

        # Remove consumer from user specific group
        await self._add_group(f'user_{self.user.id}')

        # Remove consumer from channel specific groups
        user_channels = await sync_to_async(self.get_user_channels)()
        for channel in user_channels:
            await self._remove_group(f'channel_{channel.id}')

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            event = data['event']
            data = data['data']
        except:
            await self.send_error('Invalid data')
            return

        if event == 'ping':
            await self.send(text_data=json.dumps({
                'event': 'pong',
                'data': {}
            }))
        else:
            await self.send_error('Invalid event')

    # Group methods

    async def send_notification(self, event):
        try:
            await self.send(text_data=json.dumps(event['data']))
        except:
            await self.send_error('Internal server error')

    async def add_group(self, event):
        try:
            await self._add_group(event['data']['group'])
        except:
            await self.send_error('Internal server error')

    async def remove_group(self, event):
        try:
            await self._remove_group(event['data']['group'])
        except:
            await self.send_error('Internal server error')

    # Helper methods

    def get_user_channels(self):
        return list(Channel.objects.filter(members=self.user))

    async def send_error(self, message):
        await self.send(text_data=json.dumps({
            'event': 'error',
            'data': {
                'message': message
            }
        }))

    async def _add_group(self, group):
        await self.channel_layer.group_add(
            group,
            self.channel_name
        )

    async def _remove_group(self, group):
        await self.channel_layer.group_discard(
            group,
            self.channel_name
        )