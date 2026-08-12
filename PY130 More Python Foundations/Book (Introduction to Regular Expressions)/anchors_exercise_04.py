import re

strings = [
    "A grey cat",
    "A blue caterpillar",
    "The lazy dog",
    "The white cat",
    "A loud dog",
    "--A loud dog",
    "Go away dog",
    "The ugly rat",
    "The lazy, loud dog",
]

for string in strings:
    if re.search(r'^(A|The) [a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z] (dog|cat)$', string):
        print(string)