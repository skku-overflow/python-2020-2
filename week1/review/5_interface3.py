

class Bike:
    def wheels(self):
        return 2


class BigTruck:
    def wheels(self):
        return 8


# car = Bike()
car = BigTruck()

print(car.wheels())
