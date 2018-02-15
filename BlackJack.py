import random

draw1 = random.randint(1, 11)
draw2 = random.randint(1, 11)

print('   Hi\n   I am your dealer.\n   Call me Owen.')
player = input('What is your name?')
print('Hi', player)
print('Time to start!')

print("Your hand:", draw1, draw2)
