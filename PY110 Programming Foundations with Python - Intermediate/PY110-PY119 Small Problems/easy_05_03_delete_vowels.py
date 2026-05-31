# input: list of strings
# output: new list with same string values 
# rules:
#   Explicit:
#       - Returns a list containing same string values but will all
#         the vowels(a, e, i, o, u) removed.
#       - Vowels are case insensitive. Remove 'a' and 'A' both.
#   Implicit:
#       - Empty string in a list should return empty string.
# Test Cases / Examples
#   original = ['abcdefghijklmnopqrstuvwxyz']
#   expected = ['bcdfghjklmnpqrstvwxyz']
#   print(remove_vowels(original) == expected)        # True

#   original = ['green', 'YELLOW', 'black', 'white']
#   expected = ['grn', 'YLLW', 'blck', 'wht']
#   print(remove_vowels(original) == expected)        # True

#   original = ['ABC', 'AEIOU', 'XYZ']
#   expected = ['BC', '', 'XYZ']
#   print(remove_vowels(original) == expected)        # True
# Data Struture and Algorithm:
#   - Set variable vowels to 'aeiou'
#   - Set variable deleted_vowels to empty list.
#   - Iterate for each string in the original list
#       - Initialize modified_string to empty string
#       - Iterate for each character in the string
#           - If char converted to lowercase is not in the vowels
#               keep adding char to modified_string
#       - Add modified_string to deleted_vowels
#   - Return deleted_vowels

def remove_vowels(lst):
    vowels = 'aeiou'
    deleted_vowels = []
    for string in lst:
        modified_string = ''
        for char in string:
            if char.casefold() not in vowels:
                modified_string += char
        deleted_vowels.append(modified_string)

    return deleted_vowels

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True