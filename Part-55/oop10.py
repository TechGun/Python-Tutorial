class Animal:
    def eat(self):
        print("eating..")


class Bird:
    def fly(self):
        print("flying...")


class Eagle(Animal, Bird):
    def breed(self):
        print("white-tailed eagle")


e = Eagle()
e.eat()
e.fly()
e.breed()
