import re

alphabet = re.compile("[a-zA-Z]+")

print('12345:', alphabet.findall('12345'))

# ['ffa', 'gw', 'f', 'g', 'w'] 출력
print('1ffa7gw8f7g3w:', alphabet.findall('1ffa7gw8f7g3w:'))
