
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
            # 이터레이터 루프 본문 실행

            prev = cur
            cur = s


for arr in MyIter():
    print(arr)
    # 이터레이터: 사용하는 사람이 도중에 중단 가능
    if sum(arr) > 50:
        break
