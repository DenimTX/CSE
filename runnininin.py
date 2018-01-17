import random

draw1 = random.randint(1, 11)
draw2 = random.randint(1, 11)
suitNum = random.randint(1, 4)

if suitNum == 1:
    suit = 'clubs'
if suitNum == 2:
    suit = 'spades'
if suitNum == 3:
    suit = 'diamonds'
if suitNum == 4:
    suit = 'hearts'

print('   Hi\n   I am your dealer.\n   Call me Owen.')
player = input('What is your name?')
print('Hi', player)
print('Time to start!')

print(draw1, draw2)
