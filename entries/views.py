from django.shortcuts import render
from django.views import generic
from entries import models
from entries.models import Monster, Item, Weapon, Armor, Zone


def index(request):
	return render(request, 'index.html')


class MonsterListView(generic.ListView):
	model = Monster
	template_name = 'monsters.html'


class ItemListView(generic.ListView):
	model = Item
	template_name = 'items.html'


class WeaponListView(generic.ListView):
	model = Weapon
	template_name = 'weapons.html'


class ArmorListView(generic.ListView):
	model = Armor
	template_name = 'armors.html'


class ZoneListView(generic.ListView):
	model = Zone 
	template_name = 'zones.html'