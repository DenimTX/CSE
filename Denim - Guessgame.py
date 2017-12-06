import random
# # Denim
# 1) Generate a random number between 1 and 50
# 2) Get a number (input) from the user
# 3) Compare number to input
# 4) Add "Higher" or "Lower"
# 5) Add 5 guesses
number = (random.randint(1, 50))
# print(number)   to know what the number is
print("I am thinking of a number between 1 and 50.")
guess = 5
while int(guess) != number:
    guess = input("What number am I thinking of?")
    if (int(guess)) == number:
        print("Correct")
    elif int(guess) > number:
        print("Lower.")
    elif int(guess) < number:
        print("Higher")
