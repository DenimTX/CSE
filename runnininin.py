import random


money = 15
played = 0

while money > 0:
    dice1 = (random.randint(0, 6))
    dice2 = (random.randint(0, 6))
    print("dice 1 : %s" % dice1)
    print("dice 2 : %s" % dice2)
    played += 1

    roll = (dice1 + dice2)

    if roll == 7:
        money += 4
    elif roll != 7:
        money -= 1


if money == 0:
    print("You've played %s rounds!" % str(played))
    print("You should've stopped at round %s when you had $ %s" % (tr, tm))