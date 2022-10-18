class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self):
        return f"Nieruchomość mająca {self.area} metrów i {self.rooms} pokoi. Kosztuję {self.price} zł i mieści się na " \
               f"{self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f"Dom mający {self.area} metrów i {self.rooms} pokoi. Kosztuję {self.price} zł i mieści się na " \
               f"{self.address}, z {self.plot} działką"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f"Mieszkanie mające {self.area} metrów i {self.rooms} pokoi. Kosztuję {self.price} zł i mieści się na " \
               f"{self.address}, na {self.floor} piętrze"

new_house = House(100, 4, 1000000, "Katowice, Południoa", 100)
new_flat = Flat(70, 3, 500000, "Katowice, Sokolska", 10)

print(new_house)
print(new_flat)