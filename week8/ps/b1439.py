from functools import lru_cache

S = input()
# S = "0001100"

# 01010101010
# 00010101010 => 010101010
# 010101010: 2자리 차이


# 01011110010001010 === 01010101010
# 01010101010 => 2번째 1을 뒤집으면 00010101010
# 00010101010 === 010101010


@lru_cache(maxsize=None)
def count(state):
    """
    state: 그룹 갯수.
    111000011 이면 state는 3
    """
    if state == 1:
        return 0
    if state == 2 or state == 3:
        return 1

    vals = []
    for i in range(state):
        # 첫 그룹이나 마지막 그룹을 뒤집는 경우
        if i == 0 or i == state-1:
            vals.append(count(state-1))
        else:
            vals.append(count(state-2))

    return min(vals)


def parse(s):
    initial_state = []
    cur = s[0]
    cur_cnt = 1

    for c in s[1:]:
        if c is cur:
            cur_cnt += 1
        else:
            initial_state.append(cur_cnt)
            cur = c
            cur_cnt = 1

    initial_state.append(cur_cnt)
    return initial_state


assert parse("1110011") == [3, 2, 2]
