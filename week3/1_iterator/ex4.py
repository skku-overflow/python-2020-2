
sl = ['a', 'b', 'c', 'd', 'e']

print(', '.join(sl))


print('Strip')
print('a'.strip(), 'a')
print(' b '.strip(), 'b')
print('c '.strip(), 'c')

assert ' b '.strip() == 'b'


def is_not_empty(s):
    return s.strip() != ''


sl = ['a', '  ', ' ', 'b', 'c']


print(', '.join(sl))
print(', '.join(filter(is_not_empty, sl)))
