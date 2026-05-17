# input: string
# output: list (a new list)
# rules
#   Explicit requirements:
#       - To return every substring as a element in a list 
#         that is 2 or more characters long and that is a 
#         palindromic.
#       - Palindromic detection is case sensitive ('mom' is palindromic,
#         'Mom' is not.)
#
#   Implicit requirements:
#       - Empty string should return empty list 
#
# Algorithm:
#   1. Break the strings to maximum posible substrings that are 2 or 
#      more characters long and return a list of those strings.
#           a. Fuction substrings_list:
#               1. Set start = 0 and result = []
#               2. Iterate till second last character
#                   stop = start + 2
#                   iterate till stop is less than equal to leng. of string
#                   -add string[start: stop] to result list
#                   stop += 1
#                  start += 1
#               3. Return list
#   2. Set result to empty list.
#   3. Iterate over the substrings (returned by 1st point above), check
#      if substring is a palindrome, if yes, append that substring to
#      result list.
#           a. Fuction is_palindrome:
#               1. Set idx = 0 and last_idx = -1
#               2. while idx is less then lenght of the string / 2:
#                   if string[idx] != string[last_idx]
#                       return False
#                   idx += 0
#                   last_idx -= -1
#                  return True
#   4. Return result list.  

def substrings_list(string):
    start = 0
    result = []

    while start <= (len(string) - 2):
        stop = start + 2
        while stop <= len(string):
            result.append(string[start:stop])
            stop += 1

        start += 1
    
    return result

def is_palindrome(substring):
    idx = 0
    last_idx = -1 

    while idx < (len(substring) / 2):
        if substring[idx] != substring[last_idx]:
            return False
        idx += 1
        last_idx -= 1
    
    return True


def palindrome_substrings(string):
    result = []
    for substring in substrings_list(string):
        if is_palindrome(substring):
            result.append(substring)
    
    return result

print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]
