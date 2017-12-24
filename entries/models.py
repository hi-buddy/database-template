from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=50)
    #image = models.ImageField(blank=True)
    description = models.TextField(max_length=2048)


class Monster(models.Model):
    name = models.CharField(max_length=50)
    #image = models.ImageField(blank=True)
    zones = models.ManyToManyField(Zone)
    elements = models.IntegerField()
    weakness = models.IntegerField()
    resistances = models.IntegerField()
    description = models.TextField(max_length=2048)


class Item(models.Model):
    ITEM_TYPES = (
        ('Mats', 'Materials'),
        ('Loot', 'Loot'),
        ('Other', 'Other'),
        )
    name = models.CharField(max_length=24)
    category = models.CharField(max_length=5, choices=ITEM_TYPES)
    #image = models.ImageField(blank=True)
    mats_req = models.ManyToManyField('self', blank=True)
    drop_from = models.ManyToManyField(Monster, blank=True)
    drop_chance = models.IntegerField()
    gather_quant = models.IntegerField(default=1)
    carve_spot = models.CharField(max_length=24, blank=True)
    stack_size = models.IntegerField(default=1)
    sell_value = models.IntegerField(default=1)
    buy_value = models.IntegerField(default=1)
    zones = models.ManyToManyField(Zone)
    description = models.TextField(max_length=2048)


class Weapon(models.Model):
    WEAPON_CLASSES = (
        ('GS', 'Greatsword'),
        ('SnS', 'Sword & Shield'),
        ('DB', 'Dual Blades'), 
        ('LS', 'Longsword'),
        ('Hammer', 'Hammer'),
        ('HH', 'Hunting Horn'),
        ('Lance', 'Lance'),
        ('GL', 'Gunlance'),
        ('SA', 'Switch Axe'),
        ('CB', 'Charge Blade'),
        ('IG', 'Insect Glaive'),
        ('Bow', 'Bow'),
        ('LBG', 'Light Bowgun'),
        ('HBG', 'Heavy Bowgun'),
        )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=6, choices=WEAPON_CLASSES)
    rarity = models.IntegerField(default=1)
    attack_power = models.IntegerField()
    sharpness = models.IntegerField(default=1)
    affinity = models.IntegerField(default=0)
    element = models.IntegerField(default=0)
    decorations = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)


class Armor(models.Model):
    ARMOR_CLASSES = (
        ('Helm', 'Helmet'),
        ('Chest', 'Chest'),
        ('Arms', 'Arms'),
        ('Waist', 'Waist'),
        ('Legs', 'Legs'),
        ('Charms', 'Charms'),
        ('Decorations', 'Decorations'),
        ('Palicoes', 'Palicoes'),
        )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=11, choices=ARMOR_CLASSES)
    rarity = models.IntegerField(default=1)
    defense = models.IntegerField()
    decorations = models.IntegerField(default=0)
    fire = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    lightning = models.IntegerField(default=0)
    ice = models.IntegerField(default=0)
    dragon = models.IntegerField(default=0)


class Mantle(models.Model):
    name = models.CharField(max_length=50)
    effects = models.TextField(max_length=256)
    duration = models.IntegerField()
    recharge = models.IntegerField()
    description = models.TextField(max_length=1024)