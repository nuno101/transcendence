from django.contrib import admin
from .models import User
from .models import FriendRequest
from .models import Tournament
from .models import Game

# Register your models here.
admin.site.register(User)
admin.site.register(FriendRequest)
admin.site.register(Tournament)
admin.site.register(Game)
