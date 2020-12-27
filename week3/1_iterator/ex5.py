class NotIter:
    pass

# __iter__을 구현하지 않은 클래스는 for문의 오른쪽에 올 수 없음
# for i in NotIter():
#     print(i)


class MyIter:
    def __iter__(self):
        print('Before 1')
        yield 1

        print('After 1')

        yield 2
        # 실행 끝남
        #
        # 실행이 끝났으므로 출력 X. iterator: Lazy
        print('After 2')

        yield 4

        yield 5


for i in MyIter():
    print('From loop: ', i)
    if i == 2:
        break


print('Done')
