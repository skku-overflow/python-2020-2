from functools import lru_cache


@lru_cache(maxsize=None)
def calc(n):
    # 탈출 조건
    if n == 1:
        return 1
    if n == 2:
        return 2

    return calc(n - 1) + calc(n - 2)


n = int(input())
print(calc(n) % 10007)
