import re

strings = [
    "The lazy cat sleeps",
    "The number 623 is not a cat",
    "The Alaskan drives a snowcat",
]

for string in strings:
    print(re.findall(r'\bcat$', string))