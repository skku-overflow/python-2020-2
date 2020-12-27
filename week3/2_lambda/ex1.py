def is_not_empty(s):
    return s.strip() != ''


sl = ['a', '  ', ' ', 'b', 'c']

# 이 식은, 함수 정의도 필요하고, 아래 문장만 봐선 이게 뭔지 정확히 알 수 없음
print(', '.join(filter(is_not_empty, sl)))

# 람다식 = 함수 정의
print(', '.join(filter(lambda s: s.strip() != '', sl)))
print(', '.join(filter(lambda a: a.strip() != '', sl)))


# 위에 두 개의 print문읜 완전히 같음
