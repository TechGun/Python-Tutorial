class Tata:
    def service(self):
        print("Tata car servicing done...")


class Mahindra:
    def service(self):
        print("Mahindra car servicing done...")

    def allService(self, other):
        self.service()
        other.service()


nexon = Tata()
thar = Mahindra()

thar.allService(nexon)
