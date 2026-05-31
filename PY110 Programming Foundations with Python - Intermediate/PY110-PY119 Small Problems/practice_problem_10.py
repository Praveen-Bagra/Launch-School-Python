# input: string
# output: Intetger
# rules:
#   Explicit:
#       - Original string will contain digits
#       - Returns the number of even-numbered substrings that can be
#         formed.
#       - If a substring occurs more than once, it should be counted
#         as a seperate substring.
# Test Casses / Examples
#   print(even_substrings('1432') == 6)
#   print(even_substrings('3145926') == 16)
#   print(even_substrings('2718281') == 16)
#   print(even_substrings('13579') == 0)
#   print(even_substrings('143232') == 12)
# Data Structure and Algorithm
#   - Intialize numbers = all_numbers(string) - HELPER FUNCTION
#   - Initialize variable count to 0
#   - Iterate over each number in numbers:
#       - if num is even:
#           - Increase count value by 1
#   - Return count

#   - Helper Function - all_numbers
#   - input: string
#   - output: list containing all numbers
#       - Initialize s_idx to 0
#       - Initialize numbers to empty list.
#       - Initialize length_string to length of the string
#       - while s_idx is less than length_string
#           - Initialize e_idx = s_idx + 1
#           - while e_idx is less than equal to length_string
#               - add string[s_idx:e_idx] converted to integer to numbers
#               - Increase e_idx value by 1
#           - Add s_idx value by 1
#       - Return numbers

def all_numbers(string):
    s_idx = 0
    numbers = []
    string_length = len(string)
    while s_idx < string_length:
        e_idx = s_idx + 1
        while e_idx <= string_length:
            number = int(string[s_idx:e_idx])
            numbers.append(number)
            e_idx += 1
        s_idx += 1
    
    return numbers

def even_substrings(string):
    numbers = all_numbers(string)
    even_counts = 0
    for num in numbers:
        if num % 2 == 0:
            even_counts += 1
    
    return even_counts

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

