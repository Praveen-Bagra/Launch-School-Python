import re

strings = [
        "Kx",
        "BlacK",
        "kelly",
]

for string in strings:
    if re.search('K', string):
        print(string)