




try:
    f = open('kakaotalk-config.txt', 'r')
    print('읽기 성공')
except FileNotFoundError as e:
    print('읽기 실패')
    print(e)