import random


money = 15


while money > 0:
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    print(dice1)
    print(dice2)

    roll = (dice1 + dice2)

    if roll == 7:
        (money + 4)
    elif roll != 7:
        (money - 1)
        print(money)
