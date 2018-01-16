import random

first = random.randint(1, 10)
second = random.randint(1, 10)
draw = random.randint(1, 10)
hand = 0
new = hand + draw
start = hand + first + second
print("Your hand:", start)

while hand < 22:

    answer = input("Do you want another card?")

if answer == "yes":
    print(new)
