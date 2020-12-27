# 목표: l => 짝수만 있는 리스트 생성

# 11 없음
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16]

# 손으롬
# even_list = [2, 4, 6, 8, 10, 12, 14, 16]
copied = [i for i in l]
print('Copied: ', copied)


even_list = [i for i in l if i % 2 == 0]
print('Even: ', even_list)

squared = [i * i for i in l if i % 2 == 0]
print('Even, squared: ', squared)

# 이렇게는 잘 안씀, 작동은 같음
squared_map = [i for i in map(lambda elem: elem * elem, l) if i % 2 == 0]
print('Even, squared, map: ', squared_map)
