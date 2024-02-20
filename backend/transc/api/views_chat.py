from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from .decorators import *
from .models import Channel, Message, User
from .helpers_channels import *
from .helpers_messages import *
from . import bridge_websocket as websocket

# Endpoint: /channels
@method_decorator(check_structure("/channels"), name='dispatch')
class ChannelCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    channels = Channel.objects.all().order_by("-updated_at")
    return JsonResponse([channel.serialize() for channel in channels], safe=False)
  
  def post(self, request):
    try:
      channel = Channel(name=request.json.get('name'))
      channel.full_clean()
      channel.save()
      channel.members.add(request.user)
    except ValidationError as e:
      return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
    except Exception as e:
      return JsonResponse({ERROR_FIELD: str(e)}, status=500)

    return JsonResponse(channel.serialize(), status=201)

# Endpoint: /channels/CHANNEL_ID
@method_decorator(check_structure("/channels/CHANNEL_ID"), name='dispatch')
@method_decorator(check_channel_member, name='dispatch')
class ChannelSingle(View):
  def get(self, request, channel_id):
    return JsonResponse(request.channel.serialize())
  
  def patch(self, request, channel_id):
    return update_channel(request.channel, request.json)
  
  def delete(self, request, channel_id):
    return delete_channel(request.channel)

# Endpoint: /channels/CHANNEL_ID/members
@method_decorator(check_structure("/channels/CHANNEL_ID/members"), name='dispatch')
@method_decorator(check_channel_member, name='dispatch')
class ChannelMemberCollection(View):
  def get(self, request, channel_id):
    return JsonResponse([m.serialize() for m in crequest.channel.members.all()], safe=False)
  
  def post(self, request, channel_id):
    channel = request.channel

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

    return JsonResponse([m.serialize() for m in channel.members.all()], safe=False)

# Endpoint: /channels/CHANNEL_ID/members/USER_ID
@method_decorator(check_structure("/channels/CHANNEL_ID/members/USER_ID"), name='dispatch')
@method_decorator(check_channel_member, name='dispatch')
@method_decorator(check_object_exists(User, "user_id", USER_404), name='dispatch')
class ChannelMemberSingle(View):
  def delete(self, request, channel_id, user_id):
    channel = request.channel

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

# Endpoint: /channels/CHANNEL_ID/messages
@method_decorator(check_structure("/channels/CHANNEL_ID/messages"), name='dispatch')
@method_decorator(check_channel_member, name='dispatch')
class ChannelMessageCollection(View):
  def get(self, request, channel_id):
    messages = Message.objects.filter(channel=request.channel).order_by("-created_at")
    return JsonResponse([m.serialize() for m in messages], safe=False)

  def post(self, request, channel_id):
    try:
      message = Message(channel=request.channel, author=request.user, 
                        content=parameters.get('content'))
      message.full_clean()
      message.save()
    except ValidationError as e:
      return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
    except Exception as e:
      return JsonResponse({ERROR_FIELD: str(e)}, status=500)

    websocket.send_channel_event(request.channel.id, CREATE_MESSAGE, message.serialize())

    return JsonResponse(message.serialize(), status=201)

# Endpoint: /messages
@method_decorator(check_structure("/messages"), name='dispatch')
class MessageCollection(View):
  @method_decorator(staff_required, name='dispatch')
  def get(self, request):
    messages = Message.objects.all().order_by("-created_at")
    return JsonResponse([message.serialize() for message in messages], safe=False)

# Endpoint: /messages/MESSAGE_ID
@method_decorator(check_structure("/messages/MESSAGE_ID"), name='dispatch')
@method_decorator(check_message_author, name='dispatch')
class MessageSingle(View):
  def patch(self, request, message_id):
    return update_message(request.message, request.json)
  
  def delete(self, request, message_id):
    return delete_message(request.message)