from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .decorators import login_required, check_body_syntax, check_object_exists
from .models import Channel, Message
import datetime

# Endpoint: /channels
@method_decorator(login_required, name='dispatch')
class ChannelCollection(View):
  def get(self, request):
    channels = Channel.objects.all().order_by("-updated_at")
    return JsonResponse([channel.serialize() for channel in channels], safe=False)
  
  # Creates a new channel
  @check_body_syntax(['name'])
  def post(self, request):
    channel = Channel(name=self.body.get('name'))
    channel.save()
    channel.members.add(request.user)
    return JsonResponse(channel.serialize(), status=201)

# Endpoint: /channels/<id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Channel, 'channel_id', 
																			'Channel does not exist'), name='dispatch')
class ChannelSingle(View):
  # Returns channel information by id
  def get(self, request, channel_id):
    c = Channel.objects.get(id=channel_id)
    return JsonResponse(c.serialize())
  
  @check_body_syntax(['name'])
  def patch(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    channel.name = self.body.get('name')
    channel.updated_at = datetime.datetime.now()
    channel.save()
    return JsonResponse(channel.serialize(), status=200)

  # Deletes a channel by id
  def delete(self, request, channel_id):
    Channel.objects.get(id=channel_id).delete()
    return JsonResponse({}, status=204)

# Endpoint: /channels/<id>/messages
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Channel, 'channel_id', 
																			'User does not exist'), name='dispatch')
class MessageCollection(View):
  # Returns a list of messages in a channel
  def get(self, request, channel_id):
    messages = Message.objects.filter(channel=channel_id).order_by("-created_at")
    return JsonResponse([m.serialize() for m in messages], safe=False)

  # Creates a new message in a channel
  @check_body_syntax(['content'])
  def post(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    message = Message(content=self.body.get('content'), author=request.user, 
                      channel=channel)
    message.save()

    channel.updated_at = datetime.datetime.now()
    channel.save()

    # send_to_group(f"chat_{id}", { # TODO: Implement
    #   "event": "new_message",
    #   "data": message.serialize()
    # })
    return JsonResponse(message.serialize(), status=201)

# Endpoint: /channels/<id>/messages/<mid>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Channel, 'channel_id', 
																			'User does not exist'), name='dispatch')
@method_decorator(check_object_exists(Message, 'message_id', 
																			'Message does not exist'), name='dispatch')
class MessageSingle(View):
  @check_body_syntax(['content'])
  def patch(self, request, channel_id, message_id):
    message = Message.objects.get(id=message_id)
    if message.channel.id is not channel_id:
      return JsonResponse({"reason": "Message does not exist in channel"}, status=404)

    message.content = self.body.get('content')
    message.updated_at = datetime.datetime.now()
    message.save()
    return JsonResponse(message.serialize(), status=200)
  
  # Deletes a message by id
  def delete(self, request, channel_id, message_id):
    message = Message.objects.get(id=message_id)
    if message.channel.id is not channel_id:
      return JsonResponse({"reason": "Message does not exist in channel"}, status=404)
    message.delete()

    # send_to_group(f"chat_{id}", { # TODO: Implement
    #   "event": "delete_message",
    #   "data": {
    #     "message_id": mid
    #   }
    # })
    return JsonResponse({}, status=204)