# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# print(last_name, first_name)


# first_name = input('What is your first name?')
# last_name = input('What is your last name?')
#
#
# def reverse_order(first_name, last_name):
#     print("%s %s" % (last_name, first_name))


# """Warm up #2
# Write a function called "happy_bday"
# that "sings" (prints)
# the Happy Birthday Song
#
# It must take on parameter called "name"
# """
#
#
# def happy_bday(name):
#     print("Happy birthday to you,")
#     print("Happy birthday to you,")
#     print("Happy birthday dear %s" % name)  # print("Happy birthday dear " + name)    works
#     print("Happy birthday to you!")

"""
Write a function called add_py
that takes one parameter called "name"
and prints out name.py
example:
add_py("I_ate_some") == "I_ate_some.py"
"""


def add_py(name):
    print("%s.py" % name)  # Solution 1
    # print(name + ".py")  # Solution 2


"""Write a function called "add"
which takes three parameters
and prints the sum of the numbers
"""


def add(num1, num2, num3):
    print(num1 + num2 + num3)


# add(90, 900, 9000)


def repeat(string):
    print(string)
    print(string)
    print(string)
# repeat("string")


for x in range(3):
    print("string")  # prints string three times


def date(month, day, year):
    print(str(month) + "/" + str(day) + "/" + str(year))


date(12, 8, 17)
