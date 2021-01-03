
# Stack: First in last out

# First in last out 개념
def recurse(i):
    if i > 5:
        return
    recurse(i + 1)
    print(i)


recurse(1)

# 호출 순서: recurse(1) -> recurse(2) -> recurse(3) -> recurse(4) -> recurse(5)
# 함수 종료 순서: recurse(5) -> recurse(4) -> recurse(3) -> recurse(2) -> recurse(1)
