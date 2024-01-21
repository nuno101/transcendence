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
        self.channel_name = f'user_{self.user.id}'

        # Add consumer to user specific group
        await self.add_group({'group': f'user_{self.user.id}'})

        # Add consumer to channel specific groups
        user_channels = await sync_to_async(self.get_user_channels)()
        for channel in user_channels:
            await self.add_group({'group': f'channel_{channel.id}'})

        await self.accept()

    async def disconnect(self, close_code):
        if self.user.is_anonymous:
            return

        # Remove consumer from user specific group
        await self.remove_group({'group': f'user_{self.user.id}'})

        # Remove consumer from channel specific groups
        user_channels = await sync_to_async(self.get_user_channels)()
        for channel in user_channels:
            await self.remove_group({'group': f'channel_{channel.id}'})

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
        await self.send(text_data=json.dumps(event['data']))

    async def add_group(self, event):
        await self.channel_layer.group_add(
            event['group'],
            self.channel_name
        )

    async def remove_group(self, event):
        await self.channel_layer.group_discard(
            event['group'],
            self.channel_name
        )

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