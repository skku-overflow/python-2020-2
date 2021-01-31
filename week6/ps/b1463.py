from functools import lru_cache
# 백준에서 지원 X
import sys

sys.setrecursionlimit(150000)


N = int(input())


@lru_cache(maxsize=None)
def calc(n):
    assert n > 0

    # 탈출 조건
    if n == 1:
        return 0
    if n == 3 or n == 2:
        return 1

    vals = []
    if n % 3 == 0:
        # 1 (in 1 + calc...) : 3으로 나눈다
        vals.append(1 + calc(n // 3))
    if n % 2 == 0:
        # 1 (in 1 + calc...) : 2으로 나눈다
        vals.append(1 + calc(n // 2))

    # 1 (in 1 + calc...) : 1을 뺀다
    vals.append(1 + calc(n - 1))
    return min(vals)


print(calc(N))
