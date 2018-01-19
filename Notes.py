# print("Hello World")
#
# # # # print()  # Creates a blank line
# # # # print("See if you can figure this out")
# # # # print(10 % 3)
# # #
# # # # # Variables
# # # # car_name = "Lamborguieapig"
# # # # car_type = "Beast"
# # # # car_cylinders = 8
# # # # car_mpg = 9000.1
# # # #
# # # # # Inline Printing
# # # # print("My car is the %s." % car_name)
# # # # print("My car is the %s. It is a %s" % (car_name, car_type))
# # # # Taking input
# # # # name = input("What is your name? ")
# # # # print("Hello %s." % name)
# # # # # print(name)
# # # #
# # # # age = input("How old are you? ")
# # # # print("Oh, so you're %s years old." % age)
# # # # # print(age)
# # #
# # # # Change to the file
# # #
# # #
# # # <<<<<<< HEAD
# # # def print_hw():
# # #     print("Hello World")
# # # print_hw()
# # #
# # # def say_hi(name):  # name is a "parameter
# # #     print("Hello %s." % name)
# # #     print("I hope you have a fantastic day.")
# # # say_hi("John")
# # # def birthday(age):
# # #     age += 1  # age = age + 1
# # #     print(age)
# # #
# # #
# # # say_hi("John")
# # # print("John is 15. Next year:")
# # # birthday(15)
# # #
# # # age = input("How old are you? ")
# # # print("Oh, so you're %s years old." % age)
# # # # print(age)
# # #
# # # Press Ctrl-A and Ctrl-/
# # # to comment old code
# #
# #
# # # def f(x):
# # #     return x**5 + 4 * x **4 - 17*x**2 + 4
# # #
# # #
# # # print(f(3))
# # # print(f(3) + f(5))
# # #
# # # # If statements
# # #
# # #
# # # def grade_calc(percentage):
# # #     if percentage >= 90:
# # #         return "A"
# # #     elif percentage >= 80:  # Else if
# # #         return "B"
# # #     elif percentage >= 70:
# # #         return "C"
# # #     elif percentage >= 60:
# # #         return "D"
# # #     else:
# # #         return "F"
# #
# # # Loops
# #
# #
# # # for num in range(5):
# # #     print(num + 1)

# # a = 1
# # while a < 10:
# #     print(a)
# #     a += 1
#
# #
# # response = ""
# # # while response != "Hello":
# # #     response = input("Say \"Hello\"")
# #
# # print("Hello \nWorld")  # \n means newline
# #
# #
# # import random  # imports should be at the top
# # print(random.randint(0, 6))
#
# # Comparisons
# print(1 == 1)  # Two equal signs to compare
# print(1 != 2)  # One is not equal to 2
# print(not False)  # This prints True
# print(1 == 1 and 4 <= 5)
# print(1 < 0 or 5 > 1)
#
# # Recasting
# c = '1'
# print(c == 1)  # False - C is a string, 1 is an int
# print(int(c) == 1)  # True - Compares two ints
# print(c == str(1))  # True - Compares two strings


# Lists

the_count = [1, 2, 3, 4, 5]
characters = ["Graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
print(characters[0])
print(characters[4])


print(len(characters))  # Gives you the length of the list

# Going through lists
for char in characters:
    print(char)

for num in the_count:
    print(num ** 2)

len(characters)
range(3)  # Makes a list of the numbers from 0 to 2
range(len(characters))  # Makes a list of ALL INDICES

for num in range(len(characters)):
    char = characters[num]
    print("The character at index %d is %s" % (num, char))
str1 = "Hello World!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
newStr = "".join(listOne)
print(newStr)
print(listOne[-2])  # Goes backwards

# adding stuff to a list
characters.append("Ironman/Batman/whomever you want")
print(characters)
characters.append("Pepe")

# removing things from a list
characters.remove("Carl")
print(characters)

characters.pop(6)
print(characters)

# the string class
import string  # has to be at the top
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)  # start hangman off with the player already having guessed all the punctuations and space

strTwo = 'ThIs sEntENcE iS uNuSuAL'
lowercase = strTwo.lower()
print(lowercase)
