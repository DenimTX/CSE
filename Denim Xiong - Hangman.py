import random
"""
Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Hide the word (use *)
4. Reveal letters if they have been guessed
5. Create the win condition
"""

guesses = 10

words = ["Kalista", "Jinx", "Varus", "Vayne", "Ezreal", "Caitlyn", "Sivir", "Xayah", "Lucian", "Miss Fortune"]
reveal = (random.choice(words))
print(reveal)
letters = "abcdefghijklmnopqrstuvwxyz"
while guesses > 0:
    guess = input("Guess a letter")
    if guess == reveal:
        print("hi")
    if guess != reveal:
        guesses -= 1
        print("You have %s guesses left" % guesses)


# str1 = (words[rw])          replace fix
# listOne = list(str1)
# listOne[0] = '*'
# newStr = "".join(listOne)
# print(newStr)
