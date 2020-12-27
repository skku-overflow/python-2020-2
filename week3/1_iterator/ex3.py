
# e: 원소
def add_one(e):
    return e + 1


l = [1, 2, 3, 4, 5]

print('Base')
for i in l:
    print(i)


print('Mapped')
for i in map(add_one, l):
    print(i)


print('Sum 1:', sum(l))

sl = ['a', 'b', 'c', 'd', 'e']


def append_a(e):
    return e + 'a'


print('Mapped, string')
for i in map(append_a, sl):
    print(i)
