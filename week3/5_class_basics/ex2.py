class Animal:
    def walk(self):
        print('Animal.walk')


class Dog(Animal):
    pass


class Cat(Animal):
    # 오버라이딩
    def walk(self):
        print('Cat.walk')

        # 부모 클래스의 메소드 호출
        # super().walk()


dog = Dog()
cat = Cat()

print(dog)
print(cat)

print('Dog')
dog.walk()
print('Cat')
cat.walk()
