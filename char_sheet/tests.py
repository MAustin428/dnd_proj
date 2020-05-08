from django.test import TestCase

from .models import Player, Charakter
from .views import add_player, add_char, index, char_detail
# Create your tests here.

class PlayerModelTests(TestCase):

	def test_player_is_unique(self):
		"""
		"""
		pl_list = Player.objects.all()
		assert(len(pl_list) == len(set(pl_list)))

class IndexViewTests(TestCase):

	def test_add_player(self):
		"""
		Returns True if add_player successfully creates a new instance of the Player class
		"""
		len_before = len(Player.objects.all())
		add_player('TestName')
		len_after = len(Player.objects.all())
		assert(len_after == len_before+1)
