class Human:

    def __init__(self, n, a):
        self.name = n
        self.__age = a

    def get_age(self):
        print(self.__age)


vishwajeet = Human("vishwajeet", 24)
# vishwajeet.get_age()
print(vishwajeet._Human__age)
