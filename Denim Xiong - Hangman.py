import random
"""
Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Hide the word (use *)
4. Reveal letters if they have been guessed
5. Create the win condition
"""
words = ["Zilean", "Nautilus", "Mordekaiser", "Evelynn", "Aatrox", "Swain", "Vladimir", "Alistar", "Vayne", "Ezreal"]
rw = random.randint(0, 9)
print(words[rw])

# str1 = (words[rw])          replace fix
# listOne = list(str1)
# listOne[0] = '*'
# newStr = "".join(listOne)
# print(newStr)
