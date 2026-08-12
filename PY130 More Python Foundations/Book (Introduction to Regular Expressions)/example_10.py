import re

strings = [
"Four and 20 black birds",
"365 days in a year, 100 years in a century.",
"My phone number is 222-555-1212.",
"My serial number is 345678912.",
]

for string in strings:
    print(re.findall(r'\b\d\d\d+\b', string))