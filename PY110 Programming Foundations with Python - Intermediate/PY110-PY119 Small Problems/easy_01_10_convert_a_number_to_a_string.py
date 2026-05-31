# input: integer
# output: string
# rules
#   Explicit:
#       - Convert a non-negative integer value to its string 
#         representation
#       - Not to use any standard conversion functions available
#         in Python, such as 'str'. 
#   Implicit:
#       - 0 should return '0'.
# Test Cases / Examples
#   print(integer_to_string(4321) == "4321")              # True
#   print(integer_to_string(0) == "0")                    # True
#   print(integer_to_string(5000) == "5000")              # True
#   print(integer_to_string(1234567890) == "1234567890")  # True
# Data Structure and Algorithm:
#   - Initialize numbers_dict to dictionary containing elements as:
#     {1: '1', 2: '2',....upto 0: '0'}
#   - Initialize variable 'num_str' to empty string
#   - Iterate True:
#       - initialize int_num =  num % 10 
#       - add int_num associated value from numbers_dict to num_str
#       - num //= 10
#       
#       -if num == 0:
#           break
#   - Return reversed num_str

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

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
print(integer_to_string(4) == "4")                    # True