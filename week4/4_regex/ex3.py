
# 로그 메시지가
# INFO: 2020/01/03 - GET https://skku.edu 200
# INFO: 2020/01/03 - GET https://skku.edu 200
# INFO: 2020/01/03 - GET https://skku.edu 200
# INFO: 2020/01/03 - GET https://skku.edu 200
# INFO: 2020/01/03 - POST https://skku.edu 500
# INFO: 2020/01/03 - GET https://skku.edu 200
# INFO: 2020/01/03 - GET https://skku.edu 200
# 레벨  / 날짜 / 종류 / 주소 / HTTP 응답 코드

import re

re.compile('^[INFO|DEBUG] [[0-9]{2,4}]/]...')
