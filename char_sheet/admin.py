from django.contrib import admin

# Register your models here.
from .models import Player
from .models import Charakter

admin.site.register(Player)
admin.site.register(Charakter)