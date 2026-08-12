import re

strings = [
    "To be or not to be",
    "Be a busy bee",
    "I brake for animals.",
]

for string in strings:
    print(re.findall(r'\bb[a-z]*e\b', string))