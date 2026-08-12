import re

strings = [
    "2225551212",
    "1234567890",
    "123456789",
    "12345678900",
]

print()
for string in strings:
    print(re.findall(r'\b\d{10}\b', string))

strings2 = [
    "Four and 20 black birds",
    "365 days in a year, 100 years in a century.",
    "My phone number is 222-555-1212.",
    "My serial number is 345678912.",
]

print()
for string in strings2:
    print(re.findall(r'\b\d{3,}\b', string)) 

strings3 = [
    "Bizarre",
    "a",
    "one two three four five six seven eight nine",
    "sensitive",
    "dropouts",
]

print()
for string in strings3:
    print(re.findall(r'\b[a-z]{5,8}\b', string, flags=re.I))