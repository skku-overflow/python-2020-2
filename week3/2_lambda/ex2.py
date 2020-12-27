def call(f):
    return f(1, 2, 3, 4, 5)


# 인자 개수 오류
# print(call(lambda a, b, c: a))

print(call(lambda a, b, c, d, e: a))
print(call(lambda a, b, c, d, e: [a, b, c, d, e]))
