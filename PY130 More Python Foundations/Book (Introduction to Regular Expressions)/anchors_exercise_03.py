import re

strings = [
    "reds and blues",
    "The lazy cat sleeps.",
    "The number 623 is not a word. Or is it?",
]

for string in strings:
    print(re.findall(r'\b[a-z][a-z][a-z]\b', string, flags=re.I))
