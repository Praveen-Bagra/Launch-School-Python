import re

strings = [
    "This line has spaces",
    "This,line,has,commas,",
    "No-spaces-or-commas",
]

for string in strings:
    if re.search(r'(,| )', string):
        print(string)