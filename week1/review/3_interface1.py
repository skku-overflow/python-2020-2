# 인터페이스: 약속

# 사람: 걷기 가능, 말하기 가능

def walk(human):
    human.walk()


# walk({})


class Man:
    def walk(self):
        print('Man.walk')


class Dog:
    pass


walk(Man())

# walk 정의 X
# walk(Dog())
