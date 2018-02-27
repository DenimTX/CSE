# Defining Functions
def hello_world():
    print("Hello World!")


hello_world()


def square_it(number):
    return number ** 2


for i in range(5):
    print(square_it(i))


def tip_calc(subtotal):
    tip_amt = subtotal * 0.18  # tip_amt is a local variable
    print("The tip amount in $%d" % tip_amt)
    return tip_amt


def total_bill(subtotal):
    total = subtotal + tip_calc(subtotal)
    return total


print(total_bill(100))


def distance(x1, x2, y1, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5
    return answer


print(distance(0, 3, 0, 4))


def pythagorean(a, b):  # Pythagorean Theorem
    inside = a ** 2 + b ** 2
    answer = inside ** .5
    return answer


print(pythagorean(5, 12))