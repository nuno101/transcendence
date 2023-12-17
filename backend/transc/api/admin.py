from django.contrib import admin
from .models import User
from .models import Session
from .models import Friend
from .models import Tournament
from .models import Game

# Register your models here.
admin.site.register(User)
admin.site.register(Session)
admin.site.register(Friend)
admin.site.register(Tournament)
admin.site.register(Game)
