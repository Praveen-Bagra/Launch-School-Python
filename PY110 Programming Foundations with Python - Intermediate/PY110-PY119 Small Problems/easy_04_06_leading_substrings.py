# input: string
# output: list
# rules:
#   Explicit:
#       - Returns a list containing substrings of that string.
#       - Each substring should begin with the first letter of
#         the word
#       - List should be ordered from shortest to longest.
#   Implicit
#       - Assuming empty string should return empty list.
# Test Cases / Examples:
#   print(leading_substrings('abc') == ['a', 'ab', 'abc'])
#   print(leading_substrings('a') == ['a'])
#   print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
# Data Structure and Algorithm:
#   - Set variables sub_strings to empty list.
#   - Set ending_idx = 1
#   - Iterate for the no of times as per the length of the string
#       - add string[:idx] to sub_strings            
#       - Increase ending_idx by 1.
#   - Return sub_strings

def leading_substrings(string):
#       sub_strings = []
    #   ending_idx = 1
    #   for _ in range(len(string)):
        #   sub_strings.append(string[:ending_idx])
        #   ending_idx += 1

    #   return sub_strings

    return [string[:idx + 1] for idx in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])