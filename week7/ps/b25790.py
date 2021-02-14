from functools import lru_cache


# N = int(input())
# scores = [int(input() for _ in range(N))]

N = 6
scores = [0, 10, 20, 15, 25, 10, 20]

# @lru_cache(maxsize=None)
# def calc(cur_score, cur_idx):
#     pass


@lru_cache(maxsize=None)
def calc_score(cur_idx, streak):
    """
    cur_idx: 시작점. 처음엔 0.
    streak: 지금까지 밟은 연속된 계단의 수. 처음엔 0.
    """

    if N < cur_idx:
        # 더 이상 밟을 계단이 없음
        return 0

    # 현재 계단을 밟아서 얻은 점수
    score = scores[cur_idx]

    if N == cur_idx:
        return score

    # 연속된 계단을 밟는 경우
    possible_values = [0]
    if streak != 2:
        n1 = calc_score(cur_idx + 1, streak + 1)
        possible_values.append(n1)

    if cur_idx + 2 < N:
        n2 = calc_score(cur_idx + 2, 0)
        possible_values.append(n2)

    print(cur_idx, possible_values)
    return score + max(possible_values)


print(calc_score(0, 0))
