import re

strings = [
    "strings",
    "One fish,",
    "Two fis,",
    "Red fis_",
    "Blue fish.",
    "123 456 7890",
]

number = 1
for string in strings:
    print(re.findall(r'\b\w\w\w\b', string))