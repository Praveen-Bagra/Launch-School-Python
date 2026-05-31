# input: string
# output: boolean True or False
# rules: 
#   Explicit:
#       - return true if input string is a palindrome.
#       - palindrome string is a string that reads forward and backwords same.
#       - palindrome string is case-insensitive. Both 'madam' and 'Madam'
#         are palindrome
#       - palindrome should be checked by ignoring all non-aplhanumeric
#         characters like spaces, commas, special characters. 
#         For example "Madam, I'm Adam" is a palindrome.
#   Implicit:
#       - Input string if empty will return True
# Test Cases/ Examples:
    # print(is_real_palindrome('madam') == True)           # True
    # print(is_real_palindrome('356653') == True)          # True
    # print(is_real_palindrome('356635') == False)         # True
    # print(is_real_palindrome('356a653') == True)         # True
    # print(is_real_palindrome('123ab321') == False)       # True

    # # case doesn't matter
    # print(is_real_palindrome('Madam') == True)           # True

    # # only alphanumerics matter
    # print(is_real_palindrome("Madam, I'm Adam") == True) # True
# Data Structure/ Algorithm:
#   - Initialize variable new_str to empty string.
#   - Iterate over each character in an input string.
#       If it alphanumeric, convert it into lower, and add it
#       to new_str.
#   - check and return if new_str is palindrome.

def is_palindrome(string):
    return string == string[::-1]


def is_real_palindrome(string):
    new_str = ''
    for char in string:
        if char.isalnum():
            new_str += char.casefold()

    return is_palindrome(new_str)
    



print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True