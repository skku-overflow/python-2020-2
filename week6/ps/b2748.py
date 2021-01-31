from functools import lru_cache


@lru_cache(maxsize=None)
def calc(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return calc(n - 1) + calc(n - 2)
