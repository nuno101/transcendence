from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .decorators import *
from .models import Channel, Message
import datetime

# Endpoint: /channels
@method_decorator(login_required, name='dispatch')
class ChannelCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    channels = Channel.objects.all().order_by("-updated_at")
    return JsonResponse([channel.serialize() for channel in channels], safe=False)
  
  @check_body_syntax(['name'])
  def post(self, request):
    channel = Channel(name=self.body.get('name'))
    channel.save()
    channel.members.add(request.user)
    return JsonResponse(channel.serialize(), status=201)

# Endpoint: /channels/<int:channel_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Channel, 'channel_id', 
																			'Channel does not exist'), name='dispatch')
class ChannelSingle(View):
  def get(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.user is not channel.members.all():
      return JsonResponse({"reason": "No permission view messages"}, status=403) # TODO: Maybe create decorator?
    return JsonResponse(channel.serialize())
  
  @check_body_syntax(['name'])
  def patch(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.user is not channel.members.all():
      return JsonResponse({"reason": "No permission view messages"}, status=403) # TODO: Maybe create decorator?

    channel.name = self.body.get('name')
    channel.updated_at = datetime.datetime.now()
    channel.save()
    return JsonResponse(channel.serialize(), status=200)

  def delete(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.user is not channel.members.all():
      return JsonResponse({"reason": "No permission view messages"}, status=403) # TODO: Maybe create decorator?
    channel.delete()
    return JsonResponse({}, status=204)

# Endpoint: /channels/<int:channel_id>/messages
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Channel, 'channel_id', 
																			'Channel does not exist'), name='dispatch')
class MessageCollection(View):
  def get(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.user is not channel.members.all():
      return JsonResponse({"reason": "No permission view messages"}, status=403) # TODO: Maybe create decorator?

    messages = Message.objects.filter(channel=channel_id).order_by("-created_at")
    return JsonResponse([m.serialize() for m in messages], safe=False)

  @check_body_syntax(['content'])
  def post(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.user is not channel.members.all():
      return JsonResponse({"reason": "No permission send message"}, status=403) # TODO: Maybe create decorator?

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

# Endpoint: /messages/<int:message_id>
@method_decorator(login_required, name='dispatch')
@method_decorator(check_object_exists(Message, 'message_id', 
																			'Message does not exist'), name='dispatch')
class MessageSingle(View):
  @check_body_syntax(['content'])
  def patch(self, request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user is not message.author:
      return JsonResponse({"reason": "No permission to update message"}, status=403)

    message.content = self.body.get('content')
    message.updated_at = datetime.datetime.now()
    message.save()
    return JsonResponse(message.serialize(), status=200)
  
  def delete(self, request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user is not message.author:
      return JsonResponse({"reason": "No permission to delete message"}, status=403)

    message.delete()
    # send_to_group(f"chat_{id}", { # TODO: Implement
    #   "event": "delete_message",
    #   "data": {
    #     "message_id": mid
    #   }
    # })
    return JsonResponse({}, status=204)