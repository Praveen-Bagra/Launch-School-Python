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
# Algorithm:
#   - Declare a result variable and intialize it to an empty list.
#   - Create a list named substr_list that contains all the 
#   - substrings of the input string that are at least 2 charactes long.
#   - Loop through the words in the substr_list list.
#   - It the word is  palindrome, append it to the result list.
#   - Return the result list.
#
# Create an empty list to hold the resulting substrings.
# for each index from 0 through the next to last index position
#   for each length value from 2 through the longest possible substring
#       extract the substring of that length startting at the current
#       index position
#       add the substring to our resulting list

def palindrome_substrings(s):
    result = []
    substrings_list = substring(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result



