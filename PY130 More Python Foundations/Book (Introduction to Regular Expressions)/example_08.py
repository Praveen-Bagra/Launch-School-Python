import re

strings = [
    "John Silver",
    "Randy Johnson",
    "Duke Pettijohn",
    "Joe_Johnson",
]

for string in strings:
    print(re.findall(r'\Bjohn', string, flags=re.I))
