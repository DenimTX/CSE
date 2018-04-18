import random


class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sell(self):
        if self.name in your_inv:
            print("You sell the %s for %s gold" % (self.name, self.money))
            you.money += self.money
            your_inv.remove(self.name)
        else:
            print("You don't have a %s" % self.name)

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Weapon(Item):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Weapon, self).__init__(name, money)
        self.damage = damage
        self.lifesteal = lifesteal
        self.description = description

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Consumable(Item):
    def __init__(self, heal, name, money):
        super(Consumable, self).__init__(name, money)
        self.heal = heal
        self.name = name
        self.money = money

    def use(self):
        if Hppot or Gianthppot in your_inv:
            print("You drink a %s" % self.name)
            self.heal += you.health
        else:
            print("You don't have any consumables.")

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


class Armor(Item):
    def __init__(self, health, money):
        super(Armor, self).__init__('name', money)
        self.health = health
        self.money = money

    # BUY
    def buy(self):
        if you.money >= self.money:
            print("You buy a %s." % self.name)
            you.money -= self.money
            your_inv.append(self)
        elif you.money < self.money:
            print("You don't have enough money.")


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


class Character(object):
    def __init__(self, name, health, description, attack, money, inventory):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False
        self.money = money
        self.inventory = inventory

    def take_damage(self, amount):
        self.health -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if target.health <= 0:
            target.death = True
            print('%s died.' % target.name)
            print('You received %s gold.' % target.money)
            # Loot
            choice = random.randint(1, 20)
            loot = random.randint(1, 20)
            if choice == loot:
                your_inv.append(target.inventory)
            self.money += target.money
            exit(0)

    def fight(self, enemy):
        if enemy == current_node.enemy_in:
            print(you.name + ",", you.description, "starts fighting with %s" % enemy.name + ",", enemy.description)
            enemy.health = enemy.orig_hp
            while enemy.health != 0:
                choice = random.choice([enemy, self])
                if choice == self:
                    enemy.hit(self)
                elif choice == enemy:
                    self.hit(enemy)
            print()
        else:
            print("That enemy isn't here you fool.")


class Enemy(Character):
    def __init__(self, name, health, description, attack, money, inventory, orig_hp):
        super(Enemy, self).__init__(name, health, description, attack, money, inventory)
        self.orig_hp = orig_hp


class Room(object):
    def __init__(self, name, south, west, east, north, southwest, northeast, southeast, northwest, description,
                 enemy_in):
        self.name = name
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.southwest = southwest
        self.northeast = northeast
        self.southeast = southeast
        self.northwest = northwest
        self.description = description
        self.enemy_in = enemy_in

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# longsword = Weapon('Longsword', 350, 25, 0, 'A generic longsword.\nDoes 25 damage')
# vampiric_sword = Weapon('Vampiric Sword', 900, 15, 3, 'A mysterious sword that gives you 3 health when you attack '
#                                                       'an enemy.\nDoes 15 damage.')
# giant_sword = Weapon('Giant Sword', 1300, 50, 0, 'The sword of a giant.\nDoes 50 damage.')
# excalibur = Weapon('Excalibur', 3600, 75, 0, 'A sword fit for a hero.\nDoes 75 damage.')
#
# giant_hp_pot = Consumable(200, "Giant Health Potion", 100)
# hp_pot = Consumable(100, "Health Potion", 50)
#
# viking_helmet = Armor(350, 450)
# thornmail = Armor(1000, 1100)
# giants_belt = Armor(500, 600)
# tabi_boots = Armor(200, 300)
# cloth_armor = Armor(300, 400)
# breastplate = Armor(400, 500)


your_inv = []
you = Character("Zeus", 100, "an old man", 10, 0, your_inv)
max_hp = you.health
demon = Enemy("Bull Demon King", 2000, "a giant, tough bull.", 100, 1000000, ["Excalibur", "Key"], 2000)
turtle = Enemy("Turtle", 200, "a sturdy blue turtle.", 20, 200, ["Longsword"], 200)
turtle1 = Enemy("Turtle", 200, "a sturdy blue turtle.", 20, 200, ["Longsword"], 200)
tiger = Enemy("Tiger", 400, "a ferocious white tiger.", 40, 400, ["Vampiric Sword"], 400)
minion = Enemy("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'], 50)


spawn_n = Room("Spawn (North)", None, None, None, None, None, None, "phoenix_n", None, 'You see a phoenix and a spawn '
                                                                                       'platform', None)
phoenix_n = Room("Phoenix (North)", None, None, None, None,
                 None, None, "phoenix_tower_intersection_n", "spawn_n", 'You see a path, a spawn platform, '
                                                                        'and a phoenix.', None)
phoenix_tower_intersection_n = Room("Phoenix-Tower Intersection (North)", "lane_high_middle", None, None, None,
                                    "mana_buff_camp_n", None, None, "phoenix_n", 'You see a turtle, a phoenix, and '
                                                                                 'a tower', None)
turtle_n = Room("Turtle Camp (North)", "bull_demon_king_intersection_n", None, None, None, None,
                "phoenix_tower_intersection_n", None, None, 'You see two paths and a turtle', turtle)
bull_demon_king_intersection_n = Room("Bull Demon King Intersection (North)", "bull_demon_king_intersection_s",
                                      "bull_demon_king", "lane_high_middle", "mana_buff_camp_n", None, None, None, None,
                                      'You see a turtle, a path, and a demon.', minion)
lane_high_middle = Room("Lane High Middle", "lane_middle", "bull_demon_king_intersection_n", None,
                        "phoenix_tower_intersection_n", None, None, "tiger_camp", None,
                        'You see two paths, a tower, and a tiger.', minion)
lane_middle = Room("Lane Middle", "lane_low_middle", None, "tiger_camp", "lane_high_middle", None, None,
                   None, None, 'You see two paths and a tiger.', minion)
lane_low_middle = Room("Lane Low Middle", "phoenix_tower_intersection_s", "bull_demon_king_intersection_s", None,
                       "lane_middle", None, "tiger_camp", None, None, 'You see two paths, a tower, and a demon', minion)
tiger_camp = Room("Tiger Camp", None, "lane_middle", None, None, "lane_low_middle", None, None,
                  "lane_high_middle", 'You see three paths and a tiger', tiger)
bull_demon_king_intersection_s = Room("Bull Demon King Intersection (South)", "mana_buff_camp", "bull_demon_king",
                                      "lane_low_middle", "bull_demon_king_intersection_n", None, None, None, None,
                                      'You see two paths, a turtle, and a demon', minion)
bull_demon_king = Room("Bull Demon King", None, None, None, None, None, "bull_demon_king_intersection_n",
                       "bull_demon_king_intersection_s", None, 'You see two paths and a demon', demon)
turtle_s = Room("Turtle Camp (South)", None, None, None, "bull_demon_king_intersection_s", None, None,
                "phoenix_tower_intersection_s", None, 'You see two paths and a turtle', turtle1)
phoenix_tower_intersection_s = Room("Phoenix-Tower Intersection (South)", None, None, None, "lane_low_middle",
                                    "phoenix_s", None, None, "mana_buff_camp_s",
                                    'You see a tower, a phoenix, and a turtle.', minion)
phoenix_s = Room("Phoenix (South)", None, None, None, None, "spawn_s", "phoenix_tower_intersection_s", None, None,
                 'You see a path, a spawn platform, and a phoenix.', None)
spawn_s = Room("Spawn (South)", 'end_gate', None, None, None, None, "phoenix_s", None, None,
               'You see a spawn platform and a phoenix.', None)
end_gate = Room("End Gate", None, None, None, "spawn_s", None, None, None, None, None, None)

current_node = spawn_n
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']


while True:
    print(current_node.name)
    print(current_node.description)

    if current_node == spawn_s or spawn_n:
        you.health = max_hp

    command = input('>_ ').lower().strip()

    if command == 'buy':
        shop = [Vikinghelmet, Thornmail, Giantsbelt, Tabiboots, Clotharmor, Breastplate, Hppot, Gianthppot, Excalibur,
                Giantsword, Vampiricsword, Longsword]

        # def buy(self):
        #     if you.money >= self.money:
        #         print("You buy a %s." % self.name)
        #         you.money -= self.money
        #         your_inv.append(self)
        #     elif you.money < self.money:
        #         print("You don't have enough money.")

        if current_node == spawn_n:
            print("---SHOP---"
                  "\nVIKING HELMET(0)----450 G"
                  "\nTHORNMAIL(1)--------1100 G"
                  "\nGIANTS BELT(2)------600 G"
                  "\nTABI BOOTS(3)-------300 G"
                  "\nCLOTH ARMOR(4)------400 G"
                  "\nBREASTPLATE(5)------500 G"
                  "\nHP POT(6)-----------50 G"
                  "\nGIANT HP POT(7)-----100 G"
                  "\nEXCALIBUR(8)--------3600 G"
                  "\nGIANT SWORD(9)------1300 G"
                  "\nVAMPIRIC SWORD(10)--900 G"
                  "\nLONGSWORD(11)-------350 G"
                  "\n----------")
            item_buying = input("What do you want to buy? (Type in the number)\n>_")
            you.money = 100000000
            try:
                item_buy = shop[int(item_buying)]
                if you.money >= item_buy.money:
                    print("You buy a %s." % item_buy.name)
                    your_inv.append(item_buy)
            except ValueError:
                print("That is not an item.")

    if command == 'quit':
        exit(0)

    if command == 'hp':
        print(you.health)

    if command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]

    if command == 'money':
        print(you.money)

    if command == 'help':
        print("Type 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast', 'se', 'nw', "
              "'s', 'w', 'e', 'n', 'sw', 'ne' to move.")

    if command == 'inv':
        print(your_inv)

    if command == 'fight':
        you.fight(current_node.enemy_in)

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    # else:
    #     print("Command not found.")

    print("---------------------------------------------------------------------------------------------------------"
          "-----------------------------------------")
    print()


# Test inventory
# print(you.fight(minion))
# print(your_inv)
# print(longsword.buy())
# print(your_inv)

# Print Inventory
# for inv in your_inv:
#     print('[ ' + inv.name + ' ]')

# Denim Xiong
