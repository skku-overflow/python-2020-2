

class Car:
    def __init__(self, wheels):
        self.num = wheels

    def wheels(self):
        return self.num


bike = Car(2)
normalCar = Car(4)

print(bike.wheels())
print(normalCar.wheels())
