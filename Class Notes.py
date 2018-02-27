# Defining a class
class Cat(object):
    # TWO underscore before and after
    def __init__(self, color, pattern):
        # Things that a Cat has
        self.color = color
        self.pattern = pattern
        self.state = "happy"
        self.hungry = False

    # Things that a Cat can do
    def jump(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state = "Happy"
        print("You play with the cat")


# Instantiating (creating) two cats
cute_cat = Cat("Brown", "Spots")
cute_cat2 = Cat("Gray", "No spots")

# Getting information about the cats
print(cute_cat.color)
print(cute_cat2.state)
print(cute_cat2.color)

cute_cat.jump()
print(cute_cat.state)
print(cute_cat2.state)

cute_cat.play()
print(cute_cat.state)


class Car(object):
    def __init__(self, color, brand, num_of_cylinders):
        self.color = color
        self.brand = brand
        self.cylinders = num_of_cylinders
        self.engineOn = False

    def turn_on(self):
        if self.engineOn:
            print("Nothing Happens")
        else:
            print("The engine turns on")
            self.engineOn = True

    def move_forward(self):
        if self.engineOn:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.engineOn:
            self.engineOn = False
            print("The engine turns off")
        else:
            print("Nothing happens")


mycar = Car(4, "Subaru", "Blue")


mycar.turn_on()
mycar.move_forward()
mycar.turn_off()


# is - a (inheritance)
# can (method)
# has - a (field)
