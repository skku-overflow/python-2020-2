
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
