import re

strings = [
    'Henry',
    'perch',
    'golf'
]

for string in strings:
    if re.search('h', string, flags=re.I):
        print(string)

for string in strings:
    if re.search(r'(h|H)', string):
        print(string)