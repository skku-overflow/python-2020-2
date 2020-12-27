# 소수를 받아서 제곱한 결과를 반환하는 dict 만들기

l = [2, 3, 5, 7, 9, 11, 13, 17, 19]


# 직접 손으로 작성하는 경우
# squared = {
#     2: 4,
#     # ...
# }

# 파이썬: dict([]) 문법으로 dict 초기화 가능
squared = dict([(i, i * i) for i in l])

print(squared)
