import re

strings = [
    "blueberry",
    "blackberry",
    "black berry",
    "strawberry",
]

for string in strings:
    if re.search(r'(blue|black)berry', string):
        print(string)