import random
# # Denim
# 1) Generate a random number between 1 and 50
# 2) Get a number (input) from the user
# 3) Compare number to input
# 4) Add "Higher" or "Lower"
# 5) Add 5 guesses

# Initializing Variables
number = (random.randint(1, 50))
print("I am thinking of a number between 1 and 50.")
guess = 5
guesses_made = 0


# Describes exactly ONE turn. The while loop is the Game Controller.
while int(guess) != number and guesses_made < 5:
    guess = input("What number am I thinking of?")
    if (int(guess)) == number:
        print("Correct")
    elif int(guess) > number:
        print("Lower")
        guesses_made += 1
    elif int(guess) < number:
        print("Higher")
        guesses_made += 1
if guesses_made >= 5:
    print("\nNo More Tries T.T")
