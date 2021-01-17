
class Car:
    pass


print(Car())


class WithInit:
    def __init__(self):
        self.test = 5


c = WithInit()
print(c.test)  # 5


class WithInitParam:
    def __init__(self, test):
        self.test = test


c = WithInitParam(7)
print(c.test)  # 7
