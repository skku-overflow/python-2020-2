
l = list(range(10))
print('l:', l)


l2 = [k for k in l]
print('l2:', l2)

# []: 배열 초기화
# i: 원하는 표현식
# for i in l: l의 각 원소 사용
# if: 원소에 적용할 조건
l3 = [i for i in l if i % 2 == 0]
print('l3:', l3)


l4 = [i * i for i in l if i % 2 == 0]
print('l4:', l4)
