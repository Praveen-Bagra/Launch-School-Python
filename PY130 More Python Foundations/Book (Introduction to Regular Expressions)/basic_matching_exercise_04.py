import re

strings = [
    "banana",
    "orange",
    "pineapples",
    "strawberry",
    "raspberry",
    "grappler",
]

for string in strings:
    if re.search(r'(banana|orange|apple|strawberry)', string):
        print(string)