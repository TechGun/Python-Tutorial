class Human:

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return f"{self.name} is a human object, and age of this human is {self.age}"


vishwajeet = Human("vishwajeet", 24)

print(vishwajeet)
