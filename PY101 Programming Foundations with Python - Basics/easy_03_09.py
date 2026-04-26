# input: string that may contan non-alphabetc characters
# output: a new string with all the non-alphabetic replaced by spaces.
#         If one or more non-alphabetic character appears in a row, it 
#         should be replaced only a single space. 
# Test Cases:
#   print(clean_up("---what's my +*& line?") == " what s my line ") 
# Data Structure and Algorithm:
#   a. initialize result = ''
#   b. Iterate over the characters in the string:
#           if char is alpha
#               then add char in the result
#           elif result last character is not space
#               then add space to the result
#   d. return result

def clean_up(string):
    result = ''
    for char in string:
        if char.isalpha():
            result += char
        elif result == '' or result[-1] != ' ':
            result += ' '
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True