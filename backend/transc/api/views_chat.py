from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .decorators import *
from .models import Channel, Message, User
from .helpers_channels import *
from .helpers_messages import *
from . import bridge_websocket as websocket

# Endpoint: /channels
class ChannelCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    channels = Channel.objects.all().order_by("-updated_at")
    return JsonResponse([channel.serialize() for channel in channels], safe=False)
  
  def post(self, request):
    channel = Channel(name=request.json.get('name'))
    channel.save()
    channel.members.add(request.user)
    return JsonResponse(channel.serialize(), status=201)

# Endpoint: /channels/<int:channel_id>
@method_decorator(check_channel_member, name='dispatch')
class ChannelSingle(View):
  def get(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    return JsonResponse(channel.serialize())
  
  def patch(self, request, channel_id):
    return update_channel(Channel.objects.get(id=channel_id), request.json)
  
  def delete(self, request, channel_id):
    return delete_channel(Channel.objects.get(id=channel_id))

# Endpoint: /channels/<int:channel_id>/members
@method_decorator(check_channel_member, name='dispatch')
class ChannelMemberCollection(View):
  def get(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    return JsonResponse([m.serialize() for m in channel.members.all()], safe=False)
  
  def post(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)

    # Check if user exists
    try:
      user = User.objects.get(id=request.json.get('user_id'))
    except:
      return JsonResponse({ERROR_FIELD: USER_404}, status=404)

    # Check if user is already member
    if user in channel.members.all():
      return JsonResponse({ERROR_FIELD: "User already member"}, status=400)

    # Check if user is blocked by any member
    for member in channel.members.all():
      if user in member.blocked.all():
        return JsonResponse({ERROR_FIELD: "User is blocked by a member"}, status=400)

    # Add user to channel
    channel.members.add(user)

    websocket.send_user_event(user.id, CREATE_CHANNEL, channel.serialize())
    websocket.send_channel_event(channel.id, UPDATE_CHANNEL, channel.serialize())
    websocket.add_consumer_to_group(user.id, f'channel_{channel.id}')
    # TODO: Implement notification system here
    return JsonResponse([m.serialize() for m in channel.members.all()], safe=False)

# Endpoint: /channels/<int:channel_id>/members/<int:user_id>
@method_decorator(check_channel_member, name='dispatch')
@method_decorator(check_object_exists(User, "user_id", USER_404), name='dispatch')
class ChannelMemberSingle(View):
  def delete(self, request, channel_id, user_id):
    channel = Channel.objects.get(id=channel_id)

    # Check if user is member
    user = User.objects.get(id=user_id)
    if user not in channel.members.all():
      return JsonResponse({ERROR_FIELD: "User is not a member"}, status=400)
    channel.members.remove(user)

    websocket.remove_consumer_from_group(user.id, f'channel_{channel.id}')
    websocket.send_user_event(user.id, DELETE_CHANNEL, {
      "id": channel.id })
    websocket.send_channel_event(channel.id, UPDATE_CHANNEL, channel.serialize())
    return HttpResponse(status=204)

# Endpoint: /channels/<int:channel_id>/messages
@method_decorator(check_channel_member, name='dispatch')
class ChannelMessageCollection(View):
  def get(self, request, channel_id):
    messages = Message.objects.filter(channel=channel_id).order_by("-created_at")
    return JsonResponse([m.serialize() for m in messages], safe=False)

  def post(self, request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    return create_message(channel, request.user, request.json)

# Endpoint: /messages
class MessageCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    messages = Message.objects.all().order_by("-created_at")
    return JsonResponse([message.serialize() for message in messages], safe=False)

# Endpoint: /messages/<int:message_id>
@method_decorator(check_message_author, name='dispatch')
class MessageSingle(View):
  def patch(self, request, message_id):
    message = Message.objects.get(id=message_id)
    return update_message(message, request.json)
  
  def delete(self, request, message_id):
    message = Message.objects.get(id=message_id)
    return delete_message(message)