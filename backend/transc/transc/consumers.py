import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get('user')
        if self.user.is_anonymous:
            await self.close()

        # Add user to user specific group
        self.add_group({'group': f'user_{self.user.id}'})

        # Add user to channel specific groups
        for channel in self.user.channels.all():
            self.add_group({'group': f'channel_{channel.id}'})

        await self.accept()

    async def disconnect(self, close_code):
        if self.user.is_anonymous:
            return

        # Remove user from user specific group
        self.remove_group({'group': f'user_{self.user.id}'})

        # Remove user from channel specific groups
        for channel in self.user.channels.all():
            self.remove_group({'group': f'channel_{channel.id}'})

    async def receive(self, text_data):
        # TODO: Implement or not needed? 
        # Maybe only a potential game handling websocket consumer needs to recieve?
        pass

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

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event))