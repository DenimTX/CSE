class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sell(self):
        print("You sell the %s for %s gold" % (self.name, self.money))


class Weapon(Item):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Weapon, self).__init__(name, money)
        self.damage = damage
        self.lifesteal = lifesteal
        self.description = description


class Consumable(Item):
    def __init__(self, heal, name, money):
        super(Consumable, self).__init__(name, money)
        self.heal = heal
        self.name = name
        self.money = money

    def use(self):
        print("You drink a %s" % self.name)


class Armor(Item):
    def __init__(self, health, money):
        super(Armor, self).__init__('name', money)
        self.health = health
        self.money = money


class Longsword(Weapon):
    def __init__(self):
        super(Longsword, self).__init__('Longsword', 350, 25, 0, 'A generic longsword.\nDoes 25 damage')


class Vampiricsword(Weapon):
    def __init__(self):
        super(Vampiricsword, self).__init__('Vampiric Sword', 900, 15, 3, 'A mysterious sword that gives you 3 health '
                                                                          'when you attack an enemy.\nDoes 15 damage.')


class Giantsword(Weapon):
    def __init__(self):
        super(Giantsword, self).__init__('Giant Sword', 1300, 50, 0, 'The sword of a giant.\nDoes 50 damage.')


class Excalibur(Weapon):
    def __init__(self):
        super(Excalibur, self).__init__('Excalibur', 3600, 75, 0, 'A sword fit for a hero.\nDoes 75 damage.')


class Gianthppot(Consumable):
    def __init__(self):
        super(Gianthppot, self).__init__(200, "Giant Health Potion", 100)


class Hppot(Consumable):
    def __init__(self):
        super(Hppot, self).__init__(100, "Health Potion", 50)


class Vikinghelmet(Armor):
    def __init__(self):
        super(Vikinghelmet, self).__init__(350, 450)


class Thornmail(Armor):
    def __init__(self):
        super(Thornmail, self).__init__(1000, 1100)


class Giantsbelt(Armor):
    def __init__(self):
        super(Giantsbelt, self).__init__(500, 600)


class Tabiboots(Armor):
    def __init__(self):
        super(Tabiboots, self).__init__(200, 300)


class Clotharmor(Armor):
    def __init__(self):
        super(Clotharmor, self).__init__(300, 400)


class Breastplate(Armor):
    def __init__(self):
        super(Breastplate, self).__init__(400, 500)
