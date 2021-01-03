# 사용례
# 회원가입 페이지 ->


def is_email_valid(e):
    if not '@' in e:
        return False
    # 이런 식으로 도메인, 사용자명 등 검증해야 함


def is_email_valid_using_regex(e):
    print(e)
    regex = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    return re.search(regex, e)


# 올바르지 않은 이메일
print(is_email_valid_using_regex('aaa@b'))

# 올바른 이메일
print(is_email_valid_using_regex('aaa@abcc.com'))
