# 프로세스

while True:
    # 열기만 하고 close 호출 안 함, with문도 안 씀
    f = open('./text1.txt', 'r')
    content = f.read()
    print(content)

    # 아래 코드 필수, 혹은 with 사용해야 함
    # f.close()

    # ulimit 검색하면 파일에 대해 자세히 나옴
