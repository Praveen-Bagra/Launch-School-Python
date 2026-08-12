import re

strings = [
    "What's up, doc?",
    "Say what? No way.",
    "?",
    "Who? What? Where? When? How?",
]

print()
for string in strings:
    print(re.findall(r'\?$', string))

print()
for string in strings:
    print(re.findall(r'^.*\?$', string))