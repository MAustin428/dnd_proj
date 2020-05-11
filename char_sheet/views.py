from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic

from .models import Player, Charakter
from .forms import PlayerForm, CharakterForm
# Create your views here.

def add_player(pl_name):
	np = Player(player_name = pl_name)
	np.save()

def index(request):
	if 'player_name' in request.POST:
		add_player(request.POST['player_name'])

	player_list = Player.objects.all()
	charakter_list = Charakter.objects.all()
	return render(request, 'char_sheet/index.html', {'player_list': player_list, 'charakter_list': charakter_list})

def detail(request, player_id):
	current_player = get_object_or_404(Player, pk=player_id)
	charakter_list = Charakter.objects.filter(player=get_object_or_404(Player, pk=player_id))
	return render(request, 'char_sheet/player_detail.html', {'player': current_player, 'charakter_list': charakter_list,})

#class DetailView(generic.DetailView):
#	model = Player
#	charakter_list = Charakter.objects.filter(player=get_object_or_404(Player, pk))


def char_detail(request, player_id):
	current_player = get_object_or_404(Player, pk=player_id)
	
	if request.method == 'POST':
		charakter_form = CharakterForm(request.POST)

		if charakter_form.is_valid():
			new_ch = charakter_form.save()
			player_list = Player.objects.all()
			charakter_list = Charakter.objects.all()
			return render(request, 'char_sheet/index.html', {'player_list': player_list, 'charakter_list': charakter_list})
	else:
		charakter_form = CharakterForm()
	
	charakter_list = Charakter.objects.filter(player=current_player)
	return render(request, 'char_sheet/char_detail.html', {'player': current_player, 'charakter_list': charakter_list, 'charakter_form': charakter_form})
