class Animal:
    def eat(self):
        print("eating..")


class Bird(Animal):
    def fly(self):
        print("flying...")


class Eagle(Bird):
    def breed(self):
        print("white-tailed eagle")


e = Eagle()
e.eat()
