from abc import ABC, abstractmethod


class Animal(ABC):
    def eat(self):
        print("eating..")

    @abstractmethod
    def die(self):
        pass


class Bird(Animal):
    def fly(self):
        print("flying...")

    def die(self):
        print("Bird die on land")


class Fish(Animal):
    def swim(self):
        print("swimming...")

    def die(self):
        print("Fish die in water")


b = Bird()
f = Fish()
