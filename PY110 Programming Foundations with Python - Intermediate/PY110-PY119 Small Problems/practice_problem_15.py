# input: string
# output: Integer
# rules:
#   Explicit:
#       - Returns the greatest product of four consecutive
#         digits in the string
#       - The argument will always have more than 4 digits
# Test Cases / Examples
#   print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
#   print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
#   print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
#   print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
# Data Structure and Algorithm:
#   - Initialize numbers_str = all_numbers_str(string) # HELPER FUNCTION
#   - Initialize product to 1
#   - Iterate over each num_str in numbers_str
#       - Initialize current_product to 1
#       - Iterate over each digit in num_str
#           - multiple product value to digit and save it in product
#       - If current_product > product
#           - Reassign product to current_product
#   - Return product
#
#   - HELPER FUNCTION - all_numbers_str(string)
#       - Initialize idx = 0
#       - Initialize numbers_substrings to empty list
#       - Initialize string_length to length of the string
#       - while idx is less than (string_length - 3)
#           - Initialize start_idx = idx
#           - Initialize end_idx = start_idx + 4
#           - while end_idx is less than equal to string_length
#               - add string[start_idx:end_idx] to numbers_substrings
#               - Reassign start_idx to end_idx
#               - Increase end_idx value by 4
#           - increase idx value by 1
#       - Return numbers_substrings

def all_numbers_str(string):
    idx = 0
    numbers_substrings = []
    string_length = len(string)
    while idx < (string_length - 3):
        start_idx = idx
        end_idx = start_idx + 4
        while end_idx <= string_length:
            numbers_substrings.append(string[start_idx:end_idx])
            start_idx = end_idx
            end_idx += 4
        idx += 1

    return numbers_substrings

def greatest_product(string):
    numbers_str = all_numbers_str(string)
    product = 1
    for num_str in numbers_str:
        current_product = 1
        for digit_str in num_str:
            current_product *= int(digit_str)
        if current_product > product:
            product = current_product
    
    return product

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
