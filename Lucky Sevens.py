import random


money = 15
played = 0
r = 0
most_money = 0
while money > 0:

    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    roll = (dice1 + dice2)
    print("DICE 1: %s" % dice1)
    print("DICE 2: %s" % dice2)
    played += 1
    if roll == 7:
        money += 4
        if money > most_money:
            most_money = money
            r = played
    elif roll != 7:
        money -= 1
        print("$", money)

if money == 0:
    print("You played %s rounds before you lost all your money." % str(played))
    print("You should've stopped at round %s when you had $ %s" % (r, most_money))
