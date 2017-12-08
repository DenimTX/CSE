import random

money = 15
dice1 = (random.randint(1, 6))
dice2 = (random.randint(1, 6))


print(dice1)
print(dice2)
print(dice1 + dice2)

if dice1 + dice2 == 7:
    print(money + 4)
