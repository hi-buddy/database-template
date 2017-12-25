from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=50)
    #image = models.ImageField(blank=True)
    num_camps = models.IntegerField(default=1)
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.name


class Monster(models.Model):
    name = models.CharField(max_length=50)
    #image = models.ImageField(blank=True)
    zones = models.ManyToManyField(Zone)
    elements = models.IntegerField()
    weakness = models.IntegerField()
    resistances = models.IntegerField()
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.name


class Item(models.Model):
    ITEM_TYPES = (
        ('Mats', 'Crafting'),
        ('Carve', 'Carving'),
        ('Weap', 'Weapon'),
        ('Armor', 'Armor'),
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
   
    def __str__(self):
        return self.name


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
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.name


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
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.name


class Mantle(models.Model):
    name = models.CharField(max_length=50)
    effects = models.TextField(max_length=256)
    duration = models.IntegerField()
    recharge = models.IntegerField()
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.name


class Skill(models.Model):
    SKILL_LIST = (
        ('AB', 'Attack Boost'),
        ('AD', 'Adrenaline'),
        ('AE', 'Aquatic Expert'),
        ('AS', 'Affinity Sliding'),
        ('Art', 'Artillery'),
        ('BBQ', 'BBQ Master'),
        ('BO', 'Botanist'),
        ('CH', 'Cliffhanger'),
        ('Con', 'Constitution'),
        ('DA', 'Dragon Attack'),
        ('DB', 'Defense Boost'),
        ('EE', 'Evade Extender'),
        ('Ent', 'Entomologist'),
        ('EW', 'Evade Window'),
        ('FA', 'Fire Attack'),
        ('Foc', 'Focus'),
        ('For', 'Fortify'),
        ('FR', 'Fire Resistance'),
        ('Grd', 'Guard'),
        ('HB', 'Health Boost'),
        ('HH', 'Honey Hunter'),
        ('HM', 'Horn Maestro'),
        ('HR', 'Hunger Resistance'),
        ('IA', 'Ice Attack'),
        ('Int', 'Intimidator'),
        ('IP', 'Item Prolonger'),
        ('IR', 'Ice Resistance'),
        ('JM', 'Jump Master'),
        ('MG', 'Master Gatherer'),
        ('MM', 'Master Mounter'),
        ('MR', 'Muck Resistance'),
        ('MaR', 'Marathon Runner'),
        ('Pal', 'Palico Rally'),
        ('PR', 'Paralysis Resistance'),
        ('PoR', 'Poison Resistance'),
        ('PT', 'Pro Transporter'),
        ('QS', 'Quick Shealth'),
        ('RS', 'Recovery Speed'),
        ('RU', 'Recovery Up'),
        ('SAB', 'Special Ammo Boost'),
        ('Sce', 'Scenthound'),
        ('SC', 'Slinger Capacity'),
        ('SpC', 'Speed Crawler'),
        ('SE', 'Speed Eating'),
        ('SpE', 'Sporepuff Expert'),
        ('Sl', 'Slugger'),
        ('SR', 'Stun Resistance'),
        ('SRU', 'Scoutfly Range Up'),
        ('SS', 'Stamina SurgeAttack Boost'),
        ('SpS', 'Speed Sharpening'),
        ('ST', 'Stamina Thief'),
        ('Stl', 'Stealth'),
        ('TA', 'Thunder Attack'),
        ('TR', 'Thunder Resistance'),
        ('WA', 'Water Attack'),
        ('Wi', 'Windproof'),
        ('WR', 'Water Resistance'),
        )

    SKILL_TYPES = (
        ('B', 'Basic'),
        ('SB', 'Set Bonus'),
        ('Tog', 'Toggle'),
        )

    name = models.CharField(max_length=3, choices=SKILL_LIST)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=SKILL_TYPES)
    max_rank = models.IntegerField(default=7)
    growth = models.TextField(max_length=1024)
    affixed_to = models.ManyToManyField(Armor, blank=True)

    def __str__(self):
        return self.name