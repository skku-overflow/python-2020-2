

class Vehicle:
    def __init__(self):
        self.running = False

    def run(self):
        print('Vehicle.run()')
        self.running = True

    def stop(self):
        print('Vehicle.stop()')
        self.running = False


class Car(Vehicle):
    def run(self):
        print('Starting Car.run()')
        
        super().run()

        print('Finishing Car.run()')
        


car = Car()
# bike = Bike()
# truck = Truck(6)

# cars = [car, bike, truck]
cars = [car]

# total = sum(map(lambda c: c.wheels(), cars))

# print('Total: ', total)

# assert total == 12

for car in cars:
    car.run()
    assert car.running
    car.stop()
    assert not car.running