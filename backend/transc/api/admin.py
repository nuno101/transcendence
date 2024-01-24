from django.contrib import admin
from .models import User, UserStats, FriendRequest
from .models import Tournament, Game
from .models import Channel, Message

# Register your models here.
admin.site.register(User)
admin.site.register(UserStats)
admin.site.register(FriendRequest)
admin.site.register(Tournament)
admin.site.register(Game)
admin.site.register(Channel)
admin.site.register(Message)
