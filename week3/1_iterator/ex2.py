
# dict 자료 타입
d = {
    'use': '사용하다',
    'add': '더하다',
}

# d['use']: 인덱싱
print(d['use'])
# 키 에러 (사전에 없는 단어)
# print(d['used'])

print('Keys')

# dict.keys(): 이터레이터 반환
for k in d.keys():
    print(k)

print('Range')
# range: 이터레이터 반환
for i in range(10):
    print(i)
