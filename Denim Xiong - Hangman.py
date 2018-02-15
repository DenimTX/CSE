import random
import string

"""
outline of hangman
1. make a word bank - 10 items
2. select a random item from the list
3. add user input to a list of letters_guessed
4. build a list of letters to show, and display the string form
5. create the win condition
"""

letters_guessed = list(string.punctuation + ' ')
guesses_left = 10
words = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir", "Bard",
         "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana",
         "Dr.Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio",
         "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern",
         "Janna", "Jarvan IV", "Jax", "Jayce", "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
         "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "KogMaw", "LeBlanc", "LeeSin", "Leona", "Lissandra", "Lucian",
         "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami",
         "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Quinn",
         "Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen",
         "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Tahm Kench", "Taliyah",
         "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr",
         "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong",
         "Xayah", "Xin Zhao", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

reveal = list(random.choice(words))
hidden_word = reveal
correct = list(reveal)
alphabet = list(string.ascii_lowercase)
while guesses_left > 0:

    output = []
    for letter in reveal:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append("_ ")

    if output == correct:
        print("YOU WIN!")
        exit(0)

    join = " ".join(output)
    print(join)
    print("You can choose:", alphabet)
    guess = input("Guess a letter : ").lower()
    if guess in reveal:
        guesses_left += 1
    guesses_left -= 1
    print("You have %s guesses left" % guesses_left)
    letters_guessed.append(guess)
    if guess in alphabet:
        alphabet.remove(guess)
    if guesses_left == 0:
        print("The word was %s" % reveal)
        exit(0)

# Denim Xiong
