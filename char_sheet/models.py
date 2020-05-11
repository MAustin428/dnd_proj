from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Player(models.Model):
	player_name = models.CharField(max_length=50)

	def __str__(self):
		return self.player_name

# Implementation for backgrounds TBD
#class 5e_Background(models.Model):


class Charakter(models.Model):

	class Class_Choices(models.TextChoices):
		BARBARIAN = 'BARBARIAN', _('Barbarian')
		BARD = 'BARD', _('Bard')
		CLERIC = 'CLERIC', _('Cleric')
		DRUID = 'DRUID', _('Druid')
		FIGHTER = 'FIGHTER', _('Fighter')
		MONK = 'MONK', _('Monk')
		PALADIN = 'PALADIN', _('Paladin')
		RANGER = 'RANGER', _('Ranger')
		ROGUE = 'ROGUE', _('Rogue')
		SORCERER = 'SORCERER', _('Sorcerer')
		WARLOCK = 'WARLOCK', _('Warlock')
		WIZARD = 'WIZARD', _('Wizard')

	class Race_Choices(models.TextChoices):
		DWARF = 'DWARF', _('Dwarf')
		ELF = 'ELF', _('Elf')
		HALFLING = 'HALFLING', _('Halfling')
		HUMAN = 'HUMAN', _('Human')
		DRAGONBORN = 'DRAGONBORN', _('Dragonborn')
		GNOME = 'GNOME', _('Gnome')
		HALFELF = 'HALF-ELF', _('Half-Elf')
		HALFORC = 'HALF-ORC', _('Half-Orc')
		TIEFLING = 'TIEFLING', _('Tiefling')
		GOLIATH = 'GOLIATH', _('Goliath')

	class Alignment_Choices(models.TextChoices):
		LAWFUL_GOOD = 'LG', _('Lawful Good')
		LAWFUL_NEUTRAL = 'LN', _('Lawful Neutral')
		LAWFUL_EVIL = 'LE', _('Lawful Evil')
		NEUTRAL_GOOD = 'NG', _('Neutral Good')
		TRUE_NEUTRAL = 'TN', _('True Neutral')
		NEUTRAL_EVIL = 'NE', _('Neutral Evil')
		CHAOTIC_GOOD = 'CG', _('Chaotic Good')
		CHAOTIC_NEUTRAL = 'CN', _('Chaotic Neutral')
		CHAOTIC_EVIL = 'CE', _('Chaotic Evil')

	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	char_name = models.CharField(max_length=50)
	klasse = models.CharField(max_length=10, choices=Class_Choices.choices)			#class
	niveau = models.PositiveSmallIntegerField(default=1)							#level
	rasse = models.CharField(max_length=12, choices=Race_Choices.choices)			#race
	herkunft = models.CharField(max_length= 25)										#background
	ausrichtung = models.CharField(max_length=2, choices=Alignment_Choices.choices)	#alignment
	exp = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.char_name
