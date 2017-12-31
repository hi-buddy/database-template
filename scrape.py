import urllib.request
import entries.models
from entries.models import Item

with urllib.request.urlopen('https://monsterhunterworld.wiki.fextralife.com/Crafting') as response:
    html = response.read().decode("utf-8")

response.close()

htmllist = html.split('\n')
item_list = []
item_tuples = []

for i in range(len(htmllist) - 10):
    #start of table row
    if ('<tr>' in htmllist[i]):
        #2 elements down is item
        #3 elements away is rarity
        #4 elements away is reagent 1
        #5 elements away is reagent 2
        item_name = htmllist[i+2].split()
        item_name = item_name[3].lstrip('href="/')
        item_name = item_name.rstrip('"')
        item_name = item_name.replace('+', ' ')
        if (item_name not in item_list):
            item_rarity = htmllist[i+3].lstrip('<td>').rstrip('</td>')
            item_reagent_1 = htmllist[i+4].split()
            item_reagent_1 = item_reagent_1[3].lstrip('href="/')
            item_reagent_1 = item_reagent_1.rstrip('"')
            item_reagent_1 = item_reagent_1.replace('+', ' ')
            item_reagent_2 = htmllist[i+5].split()
            if (len(item_reagent_2) > 2):
                item_reagent_2 = item_reagent_2[3].lstrip('href="/')
                item_reagent_2 = item_reagent_2.rstrip('"')
                item_reagent_2 = item_reagent_2.replace('+', ' ')
            else:
                item_reagent_2 = 'n/a'
            item_tuples.append((item_name, item_rarity, item_reagent_1, item_reagent_2))
            item_list.append(item_name)

for item in item_tuples:
    i = Item(name=item[0], 
        category='Mats',
        rarity=int(item[1]))
    i.save()
    i.mats_req = i.mats_req + (item[2] + ',')
    i.mats_req = i.mats_req + (item[3] + ',')
    i.save()

for i in range(len(htmllist) - 10):
    if ('<tr>' in htmllist[i]):
        item_name = htmllist[i+4].split()
        item_name = item_name[3].lstrip('href="/')
        item_name = item_name.rstrip('"')
        item_name = item_name.replace('+', ' ')
        if (item_name not in item_list):
            item = Item(name=item_name, category='Mats')
            item.save()
            item_list.append(item_name)
        item_name = htmllist[i+5].split()
        if(len(item_name) > 2):
            item_name = item_name[3].lstrip('href="/')
            item_name = item_name.rstrip('"')
            item_name = item_name.replace('+', ' ')
            if (item_name not in item_list):
                item = Item(name=item_name, category='Mats')
                item.save()
                item_list.append(item_name)
