import re

def mystery_math(equation):
    return re.sub(r'[+\-*/]', '?', equation)

print(mystery_math('4 + 3 - 5 = 2'))
# '4 ? 3 ? 5 = 2'

print(mystery_math('(4 * 3 + 2) / 7 - 1 = 1'))
# '(4 ? 3 ? 2) ? 7 ? 1 = 1'