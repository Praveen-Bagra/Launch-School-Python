import re

strings = [
    "What's up, doc?",
    "I tawt I taw a putty tat!",
    "Thufferin' thuccotath!",
    "Oh my darling, Clementine!",
    "Camptown ladies sing this song, doo dah.",
]

for string in strings:
    print(re.findall(r'\S+$', string))


