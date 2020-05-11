from django import forms
from django.forms import ModelForm

from .models import Player, Charakter

class PlayerForm(ModelForm):
	class Meta:
		model = Player
		fields = ['player_name']

class CharakterForm(ModelForm):
	class Meta:
		model = Charakter
		fields = ['char_name', 'rasse', 'klasse', 'herkunft', 'ausrichtung']