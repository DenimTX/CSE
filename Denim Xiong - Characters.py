import random


class Character(object):
    def __init__(self, name, inventory, health, description, attack):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False

    def take_damage(self, amount):
        self.health -= amount

    def swing(self, enemy):
        enemy.take_damage(self.attack)
        print("You attacked %s." % enemy.name)
        if enemy.health <= 0:
            enemy.death = True
            print("%s died." % enemy.name)

    def fight(self, enemy):
        print("You start a fight with $s" % enemy.name)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.swing(self)
            elif choice == enemy:
                self.swing(enemy)


you = Character('Zeus', [], 100, 'A useless old man.', random.randint(1, 10))
enemy = Character('Baron Nashor', [], 100, 'A purple and sturdy worm.', random.randint(1, 20))

you.fight(enemy)
