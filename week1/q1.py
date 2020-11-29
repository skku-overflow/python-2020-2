class Car:
    def wheels(self):
        return 4
    def run(self):
        self.running = True
    def stop(self):
        self.running = False

class Bike:
    def __init__(self):
        pass
    def wheels(self):
        return 2
    def run(self):
        self.running = True
    def stop(self):
        self.running = False

class Truck:
    def __init__(self, n):
        self.n = n
    def wheels(self):
        return self.n
    def run(self):
        self.running = True
    def stop(self):
        self.running = False

car = Car()
bike = Bike()
truck = Truck(6)
# 실행

cars = [car, bike, truck]

# 배열 생성은 상관 X
total = sum(map(lambda c: c.wheels(), cars))

print('Total: ', total)

assert total == 12

for car in cars:
    car.run()
    assert car.running
    car.stop()
    assert not car.running