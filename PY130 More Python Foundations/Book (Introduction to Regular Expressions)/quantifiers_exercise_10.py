import re

strings = [
    "123,456,789,123,345",
    "123,456,,789,123",
    "23,56,7",
    "13,45,78,23,45,34",
    "13,45,78,23,45,34,56",
]

for string in strings:
    print(re.findall(r'^(\d+,){2,5}\d+$', string))
