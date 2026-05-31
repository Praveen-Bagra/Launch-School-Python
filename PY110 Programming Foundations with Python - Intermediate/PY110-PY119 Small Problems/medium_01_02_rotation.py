# input: Integer
# output: Integer
# rules
#   Explicit:
#       - Return a number with last count digits of number rotated
#       - To perform the rotation, move the first of the digits that
#         we want to rotate to the end and shift the remaining digits
#         to the left.
# Test Cases / Examples:
#   print(rotate_rightmost_digits(735291, 2) == 735219)  # True
#   print(rotate_rightmost_digits(735291, 3) == 735912)  # True
#   print(rotate_rightmost_digits(735291, 1) == 735291)  # True
#   print(rotate_rightmost_digits(735291, 4) == 732915)  # True
#   print(rotate_rightmost_digits(735291, 5) == 752913)  # True
#   print(rotate_rightmost_digits(735291, 6) == 352917)  # True
#   print(rotate_rightmost_digits(1200, 3) == 1002)      # True
# Data Structure and Algorithm:
#   - Convert the number into string and split into 2 parts as per 
#     count.
#       first_part = from first char to char just before count
#       second_part = from count char to end of the string
#   - Rotate the 2nd part.
#       second_part = string second char to last char + string first char
#   - Add first part and second and and return it by by converting 
#     it to integer.
#       int(first_part + second_part)

def rotate_rightmost_digits(num, count):
    num_str = str(num)
    first_half = num_str[:-count]
    second_half = num_str[-count:]

    second_half = second_half[1:] + second_half[:1] # rotating second_half

    return int(first_half + second_half)

print(rotate_rightmost_digits(735291, 2)  == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True