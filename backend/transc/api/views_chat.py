from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .decorators import *
from .models import Channel, Message
from .helpers_channels import *
from .helpers_chat import *

# Endpoint: /channels
@method_decorator(login_required, name='dispatch')
class ChannelCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    channels = Channel.objects.all().order_by("-updated_at")
    return JsonResponse({'channels': [channel.serialize() for channel in channels]})
  
  @check_body_syntax(['name'])
  def post(self, request):
    channel = Channel(name=self.body.get('name'))
    channel.save()
    channel.members.add(request.user)
    return JsonResponse({'channel': channel.serialize()}, status=201)

CHANNEL_ACCESS_DECORATORS = [login_required, 
                             check_channel_member]

# Endpoint: /channels/<int:channel_id>
@method_decorator(CHANNEL_ACCESS_DECORATORS, name='dispatch')
class ChannelSingle(View):
  def get(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    return JsonResponse({'channel': channel.serialize()})
  
  @check_body_syntax(['name'])
  def patch(self, request, channel_id):
    return update_channel(Channel.objects.get(id=channel_id), self.body)

# TODO: Implement 
# Endpoint: /channels/<int:channel_id>/members
@method_decorator(CHANNEL_ACCESS_DECORATORS, name='dispatch')

# TODO: Implement 
# Endpoint: /channels/<int:channel_id>/members/<int:user_id>
@method_decorator(CHANNEL_ACCESS_DECORATORS, name='dispatch')

# Endpoint: /channels/<int:channel_id>/messages
@method_decorator(CHANNEL_ACCESS_DECORATORS, name='dispatch')
class ChannelMessageCollection(View):
  def get(self, request, channel_id):
    messages = Message.objects.filter(channel=channel_id).order_by("-created_at")
    return JsonResponse({'messages': [m.serialize() for m in messages]})

  @check_body_syntax(['content'])
  def post(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    return create_message(channel, request.user, self.body)

# Endpoint: /messages
@method_decorator(login_required, name='dispatch')
class MessageCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    messages = Message.objects.all().order_by("-created_at")
    return JsonResponse({'messages': [message.serialize() for message in messages]})

# Endpoint: /messages/<int:message_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Message, 'message_id', MESSAGE_404), name='dispatch')
class MessageSingle(View):
  @check_body_syntax(['content'])
  def patch(self, request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user is not message.author:
      return JsonResponse({ERROR_FIELD: "No permission to update message"}, status=403)
    return update_message(message, request.body)
  
  def delete(self, request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user is not message.author:
      return JsonResponse({ERROR_FIELD: "No permission to delete message"}, status=403)
    return delete_message(message)