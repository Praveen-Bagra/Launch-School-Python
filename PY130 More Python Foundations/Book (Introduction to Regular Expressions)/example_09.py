import re

strings = [
    "Four and 20 black birds",
    "365 days in a year, 100 years in a century.",
    "My phone number is 222-555-1212.",
    "My serial number is 345678912.",
]

for string in strings:
    print(re.findall(r'\b\d\d\d\d*\b', string))

strings2 = [
    "ct",
    "cot",
    "coot",
    "cooot",
]

for string in strings2:
    print(re.findall(r'co*t', string))

strings3 = [
    "15",
    "12345",
    "12342342345",
    "1234235",
]

for string in strings3:
    print(re.search(r'1(234)*5', string))