
# S = input()
S = "0001100"


def count(state):
    """
    state = 배열, 연속된 숫자의 개수 저장.
    111000011 이면 state는 [3, 4, 2]
    """
    if len(state) == 1:
        return 0
    if len(statem) == 2 or len(statem) == 3:
        return 1

    vals = []
    for i in range(len(state)):
        new_val = state[i]
        if i is not 0:

        state[i]


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

assert count([3, 2, 2]) == 1
