# input: 2 integers (num and s)
# output: a new list
# rules:
#   Explicit:
#       - Returns a list containing s number of numerical palindromes
#         that come after num.
#       - If num is a palindrome itself, it should be included in the
#         count.
#       - A palindrome is a string (thay may contain word, phrase, number,
#         or other sequence of characters) which reads the same
#         backward and forward. Example 2332, 110011
#       - Single digit number/character is not a palindrome.
#   Implicit:
#       - If s is equal to 0, return empty list.
# Test Cases / Examples:
#   - print(palindrome(6, 4)) # [11, 22, 33, 44]
#   - print(palindrome(75, 1)) # [77]
#   - print(palindrome(101, 2)) # [101, 111]
#   - print(palindrome(20, 0)) # []
# Data Structure and Algorithm:
#   - Initialize variable palindromes_lst to empty list.
#   - while length of of palindromes_lst is less than length:
#       - If num is palindrome:
#           add num to palindromes_lst
#       - Increase num value by 1
#   - Return palindromes_lst
#
# Helper function: is_palindrome
#   - convert num to string.
#   - chect if it equal to its reverse string by slicing and if length of str
#     is greater than 1. If yes, return True, else False. 

def is_palindrome(num):
    num = str(num)
    return num == num[::-1] and len(num) > 1

def palindrome(num, length):
    palindromes_lst = []
    while len(palindromes_lst) < length:
        if is_palindrome(num):
            palindromes_lst.append(num)
        num += 1
    
    return palindromes_lst

print(palindrome(6, 4)) # [11, 22, 33, 44]
print(palindrome(75, 1)) # [77]
print(palindrome(101, 2)) # [101, 111]
print(palindrome(20, 0)) # []
