from django.contrib import admin
from .models import Zone, Monster, Item, Weapon, Armor, Mantle, Skill

class ArmorAdmin(admin.ModelAdmin):
	list_display = ['name', 'category','rarity']
	ordering = ['name', 'category', 'rarity']


class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'category']
	ordering = ['name', 'category']


class MonsterAdmin(admin.ModelAdmin):
	list_display = ['name']
	ordering = ['name']


class SkillAdmin(admin.ModelAdmin):
	list_display = ['name']
	ordering = ['name']


class WeaponAdmin(admin.ModelAdmin):
	list_display = ['name', 'category']
	ordering = ['category', 'name']


class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'num_camps']
    ordering = ['name']


admin.site.register(Armor, ArmorAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Zone, ZoneAdmin)
