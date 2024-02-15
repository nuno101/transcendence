from asgiref.sync import sync_to_async
from api.models import User
import json

# cCONF: Constants for incoming websocket events (client -> server)
# Format "event": "handler"
VALID_CLIENT_EVENTS = [
  {"ping": "ping"},
]

async def ping(self, data):
  await self.send(text_data='{"event": "pong", "payload": {}}')