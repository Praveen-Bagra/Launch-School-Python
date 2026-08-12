import re

strings = [
    'snapdragon',
    'bearded dragon',
    'dragoon'
]

for string in strings:
    if re.search(r'dragon', string):
        print(string)