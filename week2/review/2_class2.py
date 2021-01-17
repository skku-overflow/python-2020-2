
class Car:
    def wheels(self):
        print('Car.wheels')
        return 4


class Bike(Car):
    def wheels(self):
        return 2


class Truck(Car):
    def wheels(self):
        print('Truck.wheels: start')
        super().wheels()
        print('Truck.wheels: end')
        return 6


car = Bike()
print(car.wheels())  # 2


truck = Truck()
print(truck.wheels())  # 6
