
def is_even(n):
    return n % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)


evens = list(filter(is_even, l))
print(evens)


def is_first_even(arg):
    a, b = arg
    return a % 2 == 0


l2 = [(1, 2), (2, 3)]

print(l2)
print(list(filter(is_first_even, l2)))
