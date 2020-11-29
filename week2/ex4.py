

# - 생성할 떄 숫자 리스트를 인자로 받습니다.

class MyList:
    def __init__(self, arr):
        self.arr = arr
    def same(self, to):
        print()
        print('self.arr =', self.arr)
        print('to =', to)
        print()
        assert self.arr == to
    def __add__(self, k):
        return MyList([elem + k for elem in self.arr])
    def __sub__(self, k):
        return MyList([elem - k for elem in self.arr])

    def __mul__(self, k):
        return MyList([elem * k for elem in self.arr])
    
    def __floordiv__(self, k):
        return MyList([elem // k for elem in self.arr])
    

l = MyList([1, 2, 3])

l.same([1, 2, 3])

# - 상수를 더하거나 뺄 수 있습니다.

r = l + 1
r.same([2, 3, 4])

#을 하면 r에 MyList([2, 3, 4]) 가 저장됩니다.


# - 상수 곱셈 / 나눗셈을 지원합니다.

s = l * 2 # [2, 4 , 6]

# 을 하면 s에 MyList([2, 4, 6]) 이 저장됩니다.

res1 = s // 2 # [1, 2, 3]


res2 = l // 2 # [0, 1, 1]

try:
    # 주석 해제된 경우 아래의 연산이 실행되지 않음
    # f = open('non-existing-file.txt', 'r')

    res2 = l // 0
    # 순서 중요 (클래스 상속)
except ZeroDivisionError as e:
    print('ZeroDivisionError 발생')
    print(e)
except ArithmeticError as e:
    print('ArithmeticError 발생')
    print(e)
except FileNotFoundError as e:
    print('FileNotFoundError 발생')
    print(e)

# - 0으로 나눌 경우 "0으로 나눌 수 없습니다" 라는 문구를 출력합니다.