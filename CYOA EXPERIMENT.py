import random


class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # BUY
    # def buy(self):
    #     if you.money >= self.money:
    #         print("You buy a %s." % self.name)
    #         you.money -= self.money
    #         your_inv.append(self)
    #     elif you.money < self.money:
    #         print("You don't have enough money.")


class Weapon(Item):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Weapon, self).__init__(name, money)
        self.damage = damage
        self.lifesteal = lifesteal
        self.description = description

        # def sell():
        #     if current_node == spawn_n:
        #         if self in your_inv:
        #             print("You sell the %s for %s gold" % (self.name, self.money))
        #             you.money += self.money
        #             your_inv.remove(self.name)
        #             if self in weapon_shop:
        #                 you.attack -= self.damage
        #                 you.lifesteal -= self.lifesteal
        #     else:
        #         print("You don't have a %s" % self.name)
    # BUY
    # def buy(self):
    #     if you.money >= self.money:
    #         print("You buy a %s." % self.name)
    #         you.money -= self.money
    #         your_inv.append(self)
    #     elif you.money < self.money:
    #         print("You don't have enough money.")


class Consumable(Item):
    def __init__(self, heal, name, money):
        super(Consumable, self).__init__(name, money)
        self.heal = heal

    def heal(self):
        if Hppot or Gianthppot in your_inv:
            print("You drink a %s" % self.name)
            self.heal += you.health
        else:
            print("You don't have any consumables.")

    # BUY
    # def buy(self):
    #     if you.money >= self.money:
    #         print("You buy a %s." % self.name)
    #         you.money -= self.money
    #         your_inv.append(self)
    #     elif you.money < self.money:
    #         print("You don't have enough money.")


class Armor(Item):
    def __init__(self, name, health, money):
        super(Armor, self).__init__(name, money)
        self.health = health

    # BUY
    # def buy(self):
    # if you.money >= self.money:
    #     print("You buy a %s." % self.name)
    #     you.money -= self.money
    #     your_inv.append(self)
    # elif you.money < self.money:
    #     print("You don't have enough money.")


class Longsword(Weapon):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Longsword, self).__init__(name, money, damage, lifesteal, description)


class Vampiricsword(Weapon):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Vampiricsword, self).__init__(name, money, damage, lifesteal, description)


class Giantsword(Weapon):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Giantsword, self).__init__(name, money, damage, lifesteal, description)


class Excalibur(Weapon):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Excalibur, self).__init__(name, money, damage, lifesteal, description)


class Gianthppot(Consumable):
    def __init__(self, heal, name, money):
        super(Gianthppot, self).__init__(heal, name, money)


class Hppot(Consumable):
    def __init__(self, heal, name, money):
        super(Hppot, self).__init__(heal, name, money)


class Vikinghelmet(Armor):
    def __init__(self, name, health, money):
        super(Vikinghelmet, self).__init__(name, health, money)


class Thornmail(Armor):
    def __init__(self, name, health, money):
        super(Thornmail, self).__init__(name, health, money)


class Giantsbelt(Armor):
    def __init__(self, name, health, money):
        super(Giantsbelt, self).__init__(name, health, money)


class Tabiboots(Armor):
    def __init__(self, name, health, money):
        super(Tabiboots, self).__init__(name, health, money)


class Clotharmor(Armor):
    def __init__(self, name, health, money):
        super(Clotharmor, self).__init__(name, health, money)


class Breastplate(Armor):
    def __init__(self, name, health, money):
        super(Breastplate, self).__init__(name, health, money)


class Character(object):
    def __init__(self, name, health, description, attack, lifesteal, money, inventory):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False
        self.lifesteal = lifesteal
        self.money = money
        self.inventory = inventory

    def take_damage(self, amount):
        self.health -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if you.health <= 0:
            print('You died.')
            exit(0)
        if target.health <= 0:
            target.death = True
            print('%s died.' % target.name)
            print('You received %s gold.' % target.money)
            print('HP: %s' % you.health)
            self.money += target.money
            # Loot
            choice = random.randint(1, 20)
            loot = random.randint(1, 20)
            if choice == loot:
                your_inv.append(target.inventory)

    def fight(self, enemy):
        try:
            if enemy == current_node.enemy_in:
                print(you.name + ",", you.description, "starts fighting with %s" % enemy.name + ",", enemy.description)
                enemy.health = enemy.orig_hp
                while enemy.health != 0:
                    choice = random.choice([enemy, self])
                    if choice == self:
                        enemy.hit(self)
                        you.health += you.lifesteal
                        if you.health > max_hp:
                            you.health = max_hp
                    elif choice == enemy:
                        self.hit(enemy)
                        enemy.health += enemy.lifesteal
                print()
        except AttributeError:
            print("There's no enemy here you fool.")


class Enemy(Character):
    def __init__(self, name, health, description, attack, lifesteal, money, inventory, orig_hp):
        super(Enemy, self).__init__(name, health, description, attack, lifesteal, money, inventory)
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


useless_item = Item('Useless Item', 0)
longsword = Longsword('Longsword', 350, 30, 0, 'A long sword.')
vampiric_sword = Vampiricsword('Vampiric Sword', 900, 15, 3, 'A mysterious sword that gives you 3 health when '
                                                             'you attack an enemy.\nDoes 15 damage.')
giant_sword = Giantsword('Giant Sword', 1300, 50, 0, 'The sword of a giant.\nDoes 50 damage.')
excalibur = Excalibur('Excalibur', 3600, 75, 0, 'A sword fit for a hero.\nDoes 75 damage.')

giant_hp_pot = Gianthppot(200, "Giant Health Potion", 100)
hp_pot = Hppot(100, "Health Potion", 50)

viking_helmet = Vikinghelmet('Viking Helmet', 350, 450)
thornmail = Thornmail('Thornmail', 1000, 1100)
giants_belt = Giantsbelt('Giants Belt', 500, 600)
tabi_boots = Tabiboots('Tabi Boots', 200, 300)
cloth_armor = Clotharmor('Cloth Armor', 300, 400)
breastplate = Breastplate('Breastplate', 400, 500)
money_bag = Item('Money bag', 100)
giant_money_bag = Item('Giant money bag', 250)


your_inv = []
max_hp = 100
max_inv = [1, 2, 3, 4, 5, 6]
key = Item('Key', 0)
you = Character("", 100, "", 10, 0, 0, your_inv)
demon = Enemy("Bull Demon King", 2000, "a giant, tough bull.", 100, 0, 1000000, giant_money_bag, 2000)
turtle = Enemy("Turtle", 200, "a sturdy blue turtle.", 20, 0, 0, money_bag, 200)
turtle1 = Enemy("Turtle", 200, "a sturdy blue turtle.", 20, 0, 0, money_bag, 200)
tiger = Enemy("Tiger", 400, "a ferocious white tiger.", 40, 0, 0, money_bag, 400)
minion = Enemy("Minion", 50, "a weak minion.", 5, 0, 50, hp_pot, 50)
Memes = Enemy('All the memes', 10000000000000, 'All the memes', 1000000000000000, 0, 100000000000000000000000000, [],
              10000000000000)
the_villain = Enemy('Evil Man', 2500, 'a wicked, foul man', 150, 0, 100, useless_item, 2500)


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
end_gate = Room("End Gate", None, None, None, "spawn_s", None, None, None, None, 'You see a path north and '
                                                                                 'a dark shadow.', None)
the_end = Room("THE END", None, None, None, 'end_gate', None, None, None, None, 'Thanks for playing!', Memes)

current_node = spawn_n
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']
all_the_commands = ['buy', 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast',
                    'se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne', 'hp', 'money', 'help', 'inv', 'fight', 'stats', 'me',
                    'sell', 'buy', 'bigheal', 'heal', 'fight evil']

character_name = input('What do you want to be named?\n>_')
you.name = character_name
character_description = input('How would you describe yourself?\na:')
you.description = ('a' + ' ' + character_description)

while True:
    print(current_node.name)
    print(current_node.description)

    if current_node == spawn_n:
        if you.health < max_hp:
            you.health = max_hp

    if len(your_inv) >= len(max_inv):
        print("Your inventory is full.")

    if current_node == end_gate:
        if excalibur in your_inv:
            end_gate.enemy_in = the_villain
            end_gate.south = 'the_end'

    command = input('>_ ').lower().strip()

    if command == 'bigheal':
        if giant_hp_pot in your_inv:
            if you.health == max_hp:
                print("You are already full hp.")
            if you.health < max_hp:
                print("You drink a giant health potion.")
                you.health += giant_hp_pot.heal
                if you.health > max_hp:
                    you.health = max_hp
            print('HP: %s' % you.health)
        if giant_hp_pot not in your_inv:
            print("You don\'t have a giant health potion.")

    if command == 'heal':
        if hp_pot in your_inv:
            if you.health == max_hp:
                print("You are already full hp.")
            if you.health < max_hp:
                print("You drink a health potion.")
                you.health += hp_pot.heal
                if you.health > max_hp:
                    you.health = max_hp
            print('HP: %s' % you.health)
        else:
            "You don\'t have a health potion."
        if hp_pot not in your_inv:
            print("You don\'t have a health potion.")

    if command == 'hp':
        print(str(you.health)+'/'+str(max_hp))

    if command == 'stats':
        print('-------------------------------')
        print('MAX HP' + ' - ' + str(max_hp))
        print('ATT' + ' - ' + str(you.attack))
        print('LS' + ' - ' + str(you.lifesteal))
        print('-------------------------------')

    if command == 'me':
        print('-------------------------------')
        print(you.name)
        print(you.description)
        print('-------------------------------')

    if command == 'buy':
        armor_shop = [viking_helmet, thornmail, giants_belt, tabi_boots, cloth_armor, breastplate]
        weapon_shop = [excalibur, giant_sword, vampiric_sword, longsword]
        shop = [viking_helmet, thornmail, giants_belt, tabi_boots, cloth_armor, breastplate, hp_pot, giant_hp_pot,
                excalibur, giant_sword, vampiric_sword, longsword]

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
            try:
                item_buy = shop[int(item_buying)]
                if you.money < item_buy.money:
                    print("You're poor go grind some more.")
                if you.money >= item_buy.money:
                    print("You buy a %s." % item_buy.name)
                    your_inv.append(item_buy)
                    you.money -= item_buy.money
                    if item_buy in armor_shop:
                        max_hp += item_buy.health
                    if item_buy in weapon_shop:
                        you.attack += item_buy.damage
                        you.lifesteal += item_buy.lifesteal
            except ValueError:
                print("That is not an item.")
        elif current_node != spawn_n:
            print('You are not in spawn.')

    if command == 'sell':
        armor_shop = [viking_helmet, thornmail, giants_belt, tabi_boots, cloth_armor, breastplate]
        weapon_shop = [excalibur, giant_sword, vampiric_sword, longsword]
        shop = [viking_helmet, thornmail, giants_belt, tabi_boots, cloth_armor, breastplate, hp_pot, giant_hp_pot,
                excalibur, giant_sword, vampiric_sword, longsword]

        if current_node == spawn_n:
            for i in your_inv:
                print('YOUR INV:')
                print('[ ' + i.name + ' ]')
            if len(your_inv) == 0:
                print([])
            print("\nVIKING HELMET(0)"
                  "\nTHORNMAIL(1)"
                  "\nGIANTS BELT(2)"
                  "\nTABI BOOTS(3)"
                  "\nCLOTH ARMOR(4)"
                  "\nBREASTPLATE(5)"
                  "\nHP POT(6)"
                  "\nGIANT HP POT(7)"
                  "\nEXCALIBUR(8)"
                  "\nGIANT SWORD(9)"
                  "\nVAMPIRIC SWORD(10)"
                  "\nLONGSWORD(11)"
                  "\n----------")
            selling = input('What do you want to sell?')
            try:
                sold = shop[int(selling)]
                if sold not in your_inv:
                    print('You don\'t have this in your inventory.')
                if sold in your_inv:
                    print('You sell a %s.' % sold.name)
                    you.money += sold.money
                    your_inv.remove(sold)
                    you.money += sold.money
                    if sold in armor_shop:
                        max_hp -= sold.health
                    if sold in weapon_shop:
                        you.attack -= sold.damage
                        you.lifesteal -= sold.lifesteal
            except ValueError:
                print('That is not an option.')

    if command == 'quit':
        exit(0)

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
        for i in your_inv:
            print('[ ' + i.name + ' ]')
        if len(your_inv) == 0:
            print([])

    if command == 'fight':
        you.fight(current_node.enemy_in)
        if you.health <= 0:
            current_node = spawn_n

    if command == 'fight evil':
        if current_node.enemy_in == the_villain and excalibur in your_inv:
            you.fight(current_node.enemy_in)
        else:
            print('You are not the chosen one.')

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    elif command not in all_the_commands:
        print("Command not found.")

    print("---------------------------------------------------------------------------------------------------------"
          "-----------------------------------------")
    print()

# Denim Xiong