from functools import lru_cache


case_count = int(input())


@lru_cache(maxsize=None)
def calc(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    # 7의 경우로 설명
    # 순서가 다르면 다른 값으로 취급하므로 중복에 대해 생각 안 해도 됨

    # 7 = 6 + 1
    # 6 만드는 방법 * 1 (마지막에 1이 오는 경우이므로 중복 X)

    # 7 = 5 + 2
    # 5 만드는 방법 * 1 (마지막에 2이 오는 경우이므로 중복 X)

    # 7 = 4 + 3
    # 4 만드는 방법 * 1 (마지막에 2이 오는 경우이므로 중복 X)

    # (4 + 3): (1 + 1 + 1 + 1) + 3
    # (6 + 1): (3 + 1 + 1 + 1) + 1
    # 서로 다름

    return calc(n - 1) + calc(n - 2) + calc(n - 3)


assert calc(4) == 7


# 입력 받는 부분

l = []
for i in range(case_count):
    l.append(calc(int(input())))

for res in l:
    print(res)
