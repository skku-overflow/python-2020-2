from functools import lru_cache


N = int(input())
scores = [int(input()) for _ in range(N)]

# N = 6
# scores = [10, 20, 15, 25, 10, 20]


# 시작 지점의 점수는 0
scores.insert(0, 0)


@ lru_cache(maxsize=None)
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

    # 마지막 계단을 밟은 경우
    if N == cur_idx:
        return score

    # 다음 계단을 밟아서 얻을 수 있는 점수를 저장하는 배열
    possible_values = [0]

    # 연속된 계단을 3개 밟는 경우 제외
    if streak != 2:
        # 1칸 올라가는 경우에는 인덱스는 1이 늘어나고, 밟은 연속된 계단의 개수 + 1
        n1 = calc_score(cur_idx + 1, streak + 1)
        possible_values.append(n1)

    # 마지막 계단 안 밟은 경우 제외
    if cur_idx + 2 <= N:
        # 2칸 올라가는 경우에는 인덱스는 2가 늘어나고, 밟은 연속된 계단의 개수는 1로 초기화.
        n2 = calc_score(cur_idx + 2, 1)
        possible_values.append(n2)

    # print(N - cur_idx, possible_values)
    return score + max(possible_values)


# 시작 지점의 인덱스: 0
# 시작 지점은 계단으로 보지 않는다고 했으므로 시작 지점에서 streak는 0
print(calc_score(0, 0))
