
def print_all(iter):
    print('Start')
    for i in iter:
        print(i)


def add_one(n):
    return n + 1


l = [1, 2, 3, 4, 5]
print_all(l)

mapped = map(add_one, l)
print_all(mapped)
