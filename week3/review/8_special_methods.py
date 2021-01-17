

class Overriden:
    def __str__(self):
        return 'Overriden'


class Default:
    pass


print(Overriden())
print(Default())
