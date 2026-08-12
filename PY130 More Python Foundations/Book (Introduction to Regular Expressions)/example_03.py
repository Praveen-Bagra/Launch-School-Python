import re

# string = 'Four score + seven'

# if re.search(r'[FX]', string):
    # print('1st match found.') 

# if re.search(r'[e+]', string):
    # print('2nd match found.') 

# if re.search(r'[adAB]', string):
    # print('3rd match found.') 

# if re.search(r'[*+]', string):
    # print('4th match found.') 

# strings = [
    # "a2",
    # "Model 640c1",
    # "a1 a2 a3 b1 b2 b3 c1 c2 c3 d1 d2 d3",
# ]

# for string in strings:
    # if re.search(r'[abc][12]', string):
        # print(string)

# strings1 = [
    # 'The United Nations',
    # 'The [eval] method',
    # 'Some^weird_stuff'
# ]

# for string in strings1:
    # if re.search(r'[A-z]', string):
        # print(string)

# strings2 = [
    # "yes",
    # "a",
    # "by",
    # "+/-",
    # "ABCXYZ",
    # "y",
    # "yyyyy",
    # "yyayy",
# ]

# for string in strings2:
    # if re.search(r'[^y]', string):
        # print(string)

text = 'xyz'
if re.search(r'^x', text):
    print('matched')