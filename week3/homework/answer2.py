
class MyIter:
    def __iter__(self):
        arr = [1]
        yield arr

        prev = 0
        cur = 1

        while True:
            s = prev + cur
            arr.append(s)
            yield arr
            prev = cur
            cur = s


for i in map(lambda arr: arr[-1], MyIter()):
    print(i)
    if i > 100:
        break

# 아래와 위 루프는 정확히 같음


def last_el(arr):
    return arr[-1]


for i in map(last_el, MyIter()):
    print(i)
    if i > 100:
        break
