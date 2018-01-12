import random


current_money = 15
played = 0
max_money = 0
total_rounds = 0
broke = False

while current_money > 0 and broke is False:
    dice1 = (random.randint(0, 6))
    dice2 = (random.randint(0, 6))
    print("dice 1 : %s" % dice1)
    print("dice 2 : %s" % dice2)
    played += 1

    roll = (dice1 + dice2)

    if roll == 7:
        current_money += 4
        if current_money > max_money:
            max_money = current_money
            total_rounds = played
    elif roll != 7:
        current_money -= 1
        print("You got $%s" % current_money)


if current_money == 0:
    print("You've played %s rounds!" % str(played))
    if max_money < 15:
        print("You should've never played this game in the first place scrub, now you have no money, get a job.")
    elif max_money > 14:
        print("You should've stopped at round %s when you had $%s" % (total_rounds, max_money))
    broke = True
