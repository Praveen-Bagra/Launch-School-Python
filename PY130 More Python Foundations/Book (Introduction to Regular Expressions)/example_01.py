import re

strings = ['s', 'sand', 'cats', 'cast', 'Mississippi', 'S', 'KANSAS']
strings2 = ['?', "What's up, doc?", 'Silence!', "What's that?"]
strings3 = ['chris:x:300', 'A thought; no, forget it.', '::::']
strings4 = ['cat', 'catalog', 'copycat', 'scatter', 'the lazy cat.', 'CAT', 'cast']
strings5 = ['The lazy cat.', 'The dog barks.', 'Down the rabbit hole.',
            'The lazy cat, chased by the barking dog', 'dives down the rabbit hole.',
            'catalog', 'The Yellow Dog', "My bearded dragon's name is Darwin"]
strings6 = ['(cat|dog)', 'bird(cat|dog)zebra', 'cat', 'dog']

# for string in strings:
    # if re.search(r's', string):
        # print(string) # s, sand, cats, cast, Mississippi

# for string in strings:
    # if re.search(r'S', string):
        # print(string) # S, KANSAS

# for string in strings2:
    # if re.search(r'\?', string):
        # print(string) # ?, What's up, doc?, What's that?

# for string in strings2:
    # if re.search(r'?', string):
        # print(string) # raise error

# for string in strings3:
    # if re.search(r':', string):
        # print(string) # chris:x:300, ::::

# for string in strings3:
    # if re.search(r' ', string):
        # print(string) # A thought; no, forget it.

# for string in strings3:
    # if re.search(r'\.', string):
        # print(string)  # A thought; no, forget it. 

# for string in strings4:
    # if re.search(r'cat', string):
        # print(string)  # A thought; no, forget it. # cat, catalog, copycat, scatter, the lazy cat.

# for string in strings5:
    # if re.search(r'(cat|dog|rabbit)', string):
        # print (string)
        # The lazy cat.
        # The dog barks.
        # Down the rabbit hole.
        # The lazy cat, chased by the barking dog
        # dives down the rabbit hole.
        # catalog

for string in strings6:
    if re.search(r'\(cat\|dog\)', string):
        print (string)
        # (cat|dog)
        # bird(cat|dog)zebra