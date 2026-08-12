my_lst = ['hello', 'hi', 'how are you']

capitalized_strings = (string.capitalize() for string in my_lst)
print(tuple(capitalized_strings))