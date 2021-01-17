
l = ['a', 'b', 'c', 'd', 'e']

d = dict([])
print(d)


d = dict([
    (0, '1')
])
print(d)

print(list(enumerate(l)))

d = dict([
    (i + 10, v) for i, v in enumerate(l)
])
print(d)
