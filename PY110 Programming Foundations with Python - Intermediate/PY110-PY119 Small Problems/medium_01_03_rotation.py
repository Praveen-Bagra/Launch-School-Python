# input: Integer
# output: Integer
# rules:
#   Explicit:
#       - Rotate maximum times possible. See test cases.
# Test Cases / Examples
#   print(max_rotation(735291) == 321579)          # True
#   print(max_rotation(3) == 3)                    # True
#   print(max_rotation(35) == 53)                  # True
#   print(max_rotation(8703529146) == 7321609845)  # True

#   # Note that the final sequence here is `015`. The leading
#   # zero gets dropped, though, since we're working with
#   # an integer.
#   print(max_rotation(105) == 15)                 # True
# Data Structure and Algorithm:
#   - Initialize variable rotated_string to empty string.
#   - Initialize variable num_str to:
#     convert num to string.
#   - Iterate for the number of times as per length of num_str:
#       - rotate the string and store it in string variable
#       - Add first digit of string to rotated_string
#       - Reassign string to string 2nd digit to last digit
#   - Return rotated_string converted into integer.

def rotate(string):
    return string[1:] + string[0]

def max_rotation(num):
    rotated_string = ''
    num_str = str(num)
    for _ in num_str:
        num_str = rotate(num_str)
        rotated_string += num_str[0]
        num_str = num_str[1:]
    
    return int(rotated_string)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True





