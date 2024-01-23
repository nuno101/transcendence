import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.models import Channel
from asgiref.sync import sync_to_async
from . import handler_consumers as handlers

# cCONF: Constans for group event handling
# Format "event": "handler"
VALID_GROUP_EVENTS = [
  {"send_notification": "send_notification"},
  {"add_group": "add_group"},
  {"remove_group": "remove_group"},
]

class Consumer(AsyncWebsocketConsumer):
    # Connection methods

    async def connect(self):
        self.groups = []
        self.user = self.scope.get('user')
        if self.user.is_anonymous:
            await self.accept()
            await self.send_error('Not logged in')
            await self.close()
            return

        # Add consumer default notification groups
        await self._add_group(f'user_{self.user.id}')
        user_channels = await sync_to_async(list)(Channel.objects.filter(members=self.user))
        for channel in user_channels:
            await self._add_group(f'channel_{channel.id}')

        # Add consumer to friend status specific groups
        # TODO: Maybe change to a more flexible solution, e.g. a subscription model to view other users status
        #       by choosing them in the frontend
        user_friends = await sync_to_async(list)(self.user.friends.all())
        for friend in user_friends:
            await self._add_group(f'user_status_{friend.id}')

        await self.accept()

    async def disconnect(self, close_code):
        if self.user.is_anonymous:
            return
        for group in self.groups:
            await self._remove_group(group)

    # Client event handling method
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            event = data['event']
            payload = data['payload']
        except:
            await self.send_error('Invalid data')
            return
        case = next((x for x in handlers.VALID_CLIENT_EVENTS if event in x), None)
        if case is None:
            await self.send_error('Invalid event')
        else:
            await getattr(handlers, case[event])(self, payload)

    async def send_notification(self, event):
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