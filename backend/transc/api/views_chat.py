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
  # Creates a DM channel for two users
  def post(self, request):
    try:
      nickname = request.json.get('nickname')

      try:
        target = User.objects.get(nickname=nickname)
      except:
        return JsonResponse({ERROR_FIELD: USER_404}, status=404)

      if request.user.id == target.id:
        return JsonResponse({ERROR_FIELD: "Can't add yourself"}, status=400)

      channels = Channel.objects.filter(members__in=[request.user])
      for channel in channels.all():
        if target in channel.members.all():
          return JsonResponse({ERROR_FIELD: "Channel with this user already exists"}, status=400)

      if request.user in target.blocked.all():
        return JsonResponse({ERROR_FIELD: "You are blocked by this user"}, status=400)

      name = f'DM-{request.user.nickname},{target.nickname}'
      if request.user.id > target.id:
        name = f'DM-{target.nickname},{request.user.nickname}'
        
      channel = Channel(name=f'DM-{request.user.nickname},{target.nickname}') 
      # Create DM channel
      channel.full_clean()
      channel.save()

      # Add members to DM channel
      channel.members.add(request.user)
      channel.members.add(target)

      websocket.add_consumer_to_group(request.user.id, f'channel_{channel.id}')
      websocket.add_consumer_to_group(target.id, f'channel_{channel.id}')
      websocket.send_user_event(target.id, CREATE_CHANNEL, channel.serialize())
      
      return JsonResponse(channel.serialize(), status=201)
    except ValidationError as e:
      return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
    except Exception as e:
      return JsonResponse({ERROR_FIELD: str(e)}, status=500)

# Endpoint: /channels/CHANNEL_ID/messages
@method_decorator(check_structure("/channels/CHANNEL_ID/messages"), name='dispatch')
@method_decorator(check_channel_member, name='dispatch')
class ChannelMessageCollection(View):
  def get(self, request, channel_id):
    messages = Message.objects.filter(channel=request.channel).order_by("-created_at")
    return JsonResponse([m.serialize() for m in messages], safe=False)

  def post(self, request, channel_id): 
    try:      
      channel = request.channel
      for member in channel.members.all():
        if request.user in member.blocked.all():
          return JsonResponse({ERROR_FIELD: "You are blocked by users in the channel"}, status=400)

      message = Message(channel=request.channel, author=request.user, 
                        content=request.json.get('content'))
      message.full_clean()
      message.save()

      channel.updated_at = message.created_at
      channel.full_clean()
      channel.save()
      
      websocket.send_channel_event(request.channel.id, CREATE_MESSAGE, message.serialize())
      return JsonResponse(message.serialize(), status=201)
    except ValidationError as e:
      return JsonResponse({"type": "object", ERROR_FIELD: e.message_dict}, status=400)
    except Exception as e:
      return JsonResponse({ERROR_FIELD: str(e)}, status=500)



# Endpoint: /messages/MESSAGE_ID
@method_decorator(check_structure("/messages/MESSAGE_ID"), name='dispatch')
@method_decorator(check_message_author, name='dispatch')
class MessageSingle(View):
  def delete(self, request, message_id):
    return delete_message(request.message)
