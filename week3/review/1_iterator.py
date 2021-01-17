
def print_all(iter):
    print('Start')
    for i in iter:
        print(i)


print_all([1, 3, 5])


print_all(set([1, 3, 5, 3, 4, 5]))

d = {
    'a': 1,
    'b': 2,
    'c': 3,
}

print_all(d.keys())
print_all(d.values())
print_all(d.items())

for k, v in d.items():
    print('Key:', k, 'Value:', v)

# print_all(range(100000000000000000000000000000000000))
