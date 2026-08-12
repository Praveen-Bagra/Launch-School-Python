import re

strings = [
    "Mississippi",
    "ziti 0minimize7",
    "inviting illegal iridium",
]

for string in strings:
    print(re.findall(r'\b[a-z]*i[a-z]*i[a-z]*i[a-z]*\b', string, flags=re.I))