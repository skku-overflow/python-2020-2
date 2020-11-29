

def verify(s):
    if 6 <= len(s) <= 12:
        return True, ""

    return False, "입력한 값이 올바르지 않습니다"


success, msg = verify("1000000")
# success, msg = verify("100000000258y7034957823")

print('success:', success)
print('msg:', msg)
