import re

strings = [
    "The lazy cat sleeps.",
    "The number 623 is not a word.",
    "Then, we went to the movies.",
    "Ah. The bus has arrived.",
]

for string in strings:
    print(re.findall(r'^The\b', string))