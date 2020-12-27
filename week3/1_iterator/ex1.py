print('List')
l = [1, 3, 5, 7, 9]

# l: 배열, for문이 작동하는 건 l이 이터레이터
# (배열이 이터레이터의 한 종륨)
for i in l:
    print(i)

print('Set')

# set은 중복을 허용하지 않음.
# set도 이터레이터 => for문의 오른쪽에 올 수 있음
s = set([1, 2, 3, 4, 5, 1, 2, 3])

for i in s:
    print(i)
