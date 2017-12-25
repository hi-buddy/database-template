from django.shortcuts import render, get_object_or_404
from django.views import generic
from entries import models
from entries.models import Monster, Item, Weapon, Armor, Zone


def index(request):
	return render(request, 'index.html')


def detail_view(request, category, query):
	c = category.lower()
	context = {}
	if (c == 'items' and Item.objects.get(name__iexact=query) != None):
		q = Item.objects.get(name__iexact=query)
		context['query'] = q
	elif (c == 'monsters' and Monster.objects.get(name__iexact=query) != None):
		q = Monster.objects.get(name__iexact=query)
		context['query'] = q
	elif (c == 'weapons' and Weapon.objects.get(name__iexact=query) != None):
		q = Weapon.objects.get(name__iexact=query)
		context['query'] = q
	elif (c == 'armors' and Armor.objects.get(name__iexact=query) != None):
		q = Armor.objects.get(name__iexact=query)
		context['query'] = q
	elif (c == 'zones' and Zone.objects.get(name__iexact=query) != None):
		q = Zone.objects.get(name__iexact=query)
		context['query'] = q
	else:
		context['query'] = None
	if (context['query'] == None):
		return render(request, 'error.html')
	else:
		return render(request, 'detail.html', context)


def category_view(request, category):
	context = {}
	c = category.lower()
	if ((c == 'items') or
		(c == 'monsters') or
		(c == 'weapons') or
		(c == 'armors') or
		(c == 'zones')):
		context['category'] = category.title()
		return render(request, 'category.html', context)
	else:
		return render(request, 'error.html', context)
