class Human:

    def __init__(self, f, l, a):
        self.first_name = f
        self.last_name = l
        self.age = a


vishwajeet = Human("vishwajeet", "kumar", 24)
ajit = Human("ajit", "kumar", 18)

vishwajeet.programming = "c, c++, java, python"

print(vishwajeet.programming)
