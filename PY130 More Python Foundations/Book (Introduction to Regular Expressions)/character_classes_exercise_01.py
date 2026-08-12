import re

strings = [
    "Kitchen Kaboodle",
    "Reds and blues",
    "kitchen Servers",
]

for string in strings:
    if re.search(r'[kKs]', string):
        print(string)