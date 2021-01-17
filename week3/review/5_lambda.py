
def is_not_empty(s):
    return s.strip() != ''


l = ['234', '  asdnjla', '     ', '']

# 아래의 람다식은 공백 제외하고 반환
print(list(map(lambda s: s.strip(), l)))


print(list(filter(is_not_empty, l)))

# 아래의 람다식은 공백 빼고 다른 값이 반환하면 True 반환
print(list(filter(lambda s: s.strip() != '', l)))

# 아래의 람다식은 공백 빼고 다른 값이 반환하면 False 반환
print(list(filter(lambda s: s.strip() == '', l)))
