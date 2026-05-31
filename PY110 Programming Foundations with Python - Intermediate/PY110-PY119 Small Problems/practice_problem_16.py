# input: string
# output: Integer
# rules
#   Explicit
#       - Returns the count of distinct case-insensiive alphabetic
#         characters and numeric digits that occur more than once
#         in the input string.
# Test Cases / Examples
#   print(distinct_multiples('xyz') == 0)               # (none)
#   print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
#   print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
#   print(distinct_multiples('unununium') == 2)         # u, n
#   print(distinct_multiples('multiplicity') == 3)      # l, t, i
#   print(distinct_multiples('7657') == 1)              # 7
#   print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
#   print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
# Data Structure and Algorithm:
#   - Helper function, which would return char and their account.
#   - Convert string to lowercase and save it in string.
#   - char_and_counts = return_char_and_counts(strting)
#   - initialize more_than_once to:
#     [char for char in char_counts if char_and_counts[char] > 1]
#   - return length of the char_and_counts

# Helper Function: return_char_and_counts(string)
#   - Initialize char_and_counts to empty dictionary
#   - Iterate over each char in string:
#       - if char as key is in char_and_counts:
#           - Increase its associated value by 1
#       - Otherwise
#           - Insert char as key and value as 1 in char_and_counts
#   - Return char_and_counts

def return_char_and_counts(string):
    char_and_counts = {}
    for char in string:
        if char in char_and_counts:
            char_and_counts[char] += 1
        else:
            char_and_counts[char] = 1
    
    return char_and_counts

def distinct_multiples(string):
    string = string.casefold()
    char_and_counts = return_char_and_counts(string)
    more_than_once = [char for char in char_and_counts 
                           if char_and_counts[char] > 1]

    return len(more_than_once)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
