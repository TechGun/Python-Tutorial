class Human:

    def __init__(self, f, l, a):
        self.first_name = f
        self.last_name = l
        self.age = a

    def full_name(self):
        print(f"full name = {self.first_name} {self.last_name}")

    def change_age(self, newage):
        self.age = newage


vishwajeet = Human("vishwajeet", "kumar", 24)

vishwajeet.change_age(18)
vishwajeet.age = 20
print(vishwajeet.age)
