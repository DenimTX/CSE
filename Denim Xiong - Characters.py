class Character(object):
    def __init__(self, name, inventory, health, stats, description):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.stats = stats
        self.description = description

zeus = Character("Zeus", [], 100, [], 'An Old And Useless Man')
zeus.take_damage

    def take_damage(self, amount):


    def fight(self, target):


    def death(self, health):
