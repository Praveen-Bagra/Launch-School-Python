# input: string
# output: tuple
# rules
#     - Original string will be non-empty.
#     - To return a tuple conisting of a string and an integer.
#     - The equation is:
#       Original string
#       Retruned tuple (substring, inteter)
#       string == substring * integer.
#     - The original string will always contain lowercase alphabetic
#       letters.
#     - The values of substring and integer should be the shortest
#       possible substring and largest possible repeat count that
#       satisfies this equation.
# Test Cases / Examples
#   print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
#   print(repeated_substring('xyxy') == ('xy', 2))
#   print(repeated_substring('xyz') == ('xyz', 1))
#   print(repeated_substring('aaaaaaaa') == ('a', 8))
#   print(repeated_substring('superduper') == ('superduper', 1))
# Data Structure and Algorithm:
#   - Initialize substrings = all_substrings(string)
#   - Iterate over each substring:
#       - Initialize count to:
#         count substring in original string
#       - If substring * count == original string
#           return (substring, count)

# Helper Function - (all _substrings)
#   - Initialize start_idx to 0
#   - Initialize end_idx to 1
#   - Initialize substrings to empty list
#   - while end_idx is less than equal to length of the string
#       - add string[stard_idx:end_idx] to substrings.
#       - Increase end_idx value by 1
#   - Return substrings

def all_substrings(string):
    stard_idx = 0
    end_idx = 1
    substrings = []
    while end_idx <= len(string):
        substrings.append(string[stard_idx:end_idx])
        end_idx += 1
    
    return substrings

def repeated_substring(string):
    substrings = all_substrings(string)
    for substring in substrings:
        count = string.count(substring)
        if substring * count == string:
            return (substring, count)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))