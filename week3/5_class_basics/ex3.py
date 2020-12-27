# 특수 메소드 사용례
# __이름__ : 특수 메소드

class Overriden:
    def __str__(self):
        return 'Overriden'


class Default:
    pass


print(Overriden())
print(Default())
