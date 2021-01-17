

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('0으로 나눌 수 없습니다')
    print('A', a, 'B', b)
    return a//b


print(divide(100, 10))  # 10

try:
    divide(100, 0)
except ZeroDivisionError as e:
    print('Zero', e)
except ArithmeticError as e:
    print('Arith', e)

# 순서 중요 (상속 관계)

try:
    divide(100, 0)
except ArithmeticError as e:
    print('Arith', e)
except ZeroDivisionError as e:
    print('Zero', e)

print('Done')
