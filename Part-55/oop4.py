class Human:

    country = "India"

    def __init__(self, f, l, a):
        self.first_name = f
        self.last_name = l
        self.age = a
        self.state = "Assam"


vishwajeet = Human("vishwajeet", "kumar", 24)
ajit = Human("ajit", "kumar", 18)

vishwajeet.country = "US"
Human.country = "abc"
print(vishwajeet.country)
print(ajit.country)
