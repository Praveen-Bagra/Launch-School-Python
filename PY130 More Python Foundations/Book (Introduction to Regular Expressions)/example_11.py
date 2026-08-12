import re

string = "Scott scoots but doesn't act cooot"
print(re.findall(r'coo?t', string))

strings2 = [
    "20170111",
    "2017-01-11",
    "2017-0111",
    "201701-11",
]

for string in strings2:
    print(re.findall(r'\b\d\d\d\d-?\d\d-?\d\d', string))