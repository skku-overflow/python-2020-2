scores = [1, 6, 5, 6, 7, 8, 9, 3, 2, 1, 1]


def add_1(n):
    return n + 1


# list 아님. 주의!
# map은 interator 반환
m = map(add_1, scores)
print(m)

print(list(m))
