# class : blueprint for creating a new object
# Object: instance of class

# Class: Human
# Object: vishwajeet, ajit

# property/features = Attribute
# function = method


class Human:

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def eat(self):
        print("Eating...")

    def walk(self):
        print("Walking...")


vishwajeet = Human("vishwajeet", 24)
ajit = Human("ajit", 18)
print(vishwajeet.age)
