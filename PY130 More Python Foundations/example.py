import re

string = '123456789'

print(re.findall(r'[^01234567]', string))