# input: integer
# output: string
# rules
#   Explicit:
#       - Convert a  integer value to its string 
#         representation with sign. 
#       - If there is no sign to number. it means it is positive,
#         so add + to its string representation.
#       - Not to use any standard conversion functions available
#         in Python, such as 'str'. 
#       - We can use previous exercise funciton.
#   Implicit:
#       - 0 should return '0'.
# Test Cases / Examples
#   print(signed_integer_to_string(4321) == "+4321")  # True
#   print(signed_integer_to_string(-123) == "-123")   # True
#   print(signed_integer_to_string(0) == "0")         # True
# Data Structure and Algorithm:
#   - If number is less than 0:
#       number *= -1
#       return '-' + integer_to_string(number)
#   - if number is 0:
#       return integer_to_string(number)
#   - else
#       return '+' + integer_to_string(number)

def integer_to_string(number):
    numbers_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                    6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}
    num_str = ''
    while True:
        int_num = number % 10
        num_str += numbers_dict[int_num]
        number //= 10
        
        if number == 0:
            break

    return num_str[::-1]

def signed_integer_to_string(number):
    if number < 0:
        number *= -1
        return '-' + integer_to_string(number)
    elif number == 0:
        return integer_to_string(number)
    else:
        return '+' + integer_to_string(number)
        
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True