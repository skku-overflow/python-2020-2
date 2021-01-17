

def divide(a, b):
    if b == 0:
        raise ArithmeticError('0으로 나눌 수 없습니다')
    return a//b


print(divide(100, 10))  # 10

print(divide(100, 0))  # 에러
