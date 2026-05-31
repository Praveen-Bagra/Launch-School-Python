# input: Integer
# output: Integer
# rules:
#   Explicit:
#       - To return the sum of all the multiples of 7 or 11 that are less
#         than the argument.
#       - If a number is a multiple of both 7 and 11, count if just once.
#       - If the argument is negative, return 0
# Test Cases / Examples
#   print(seven_eleven(10) == 7)
#   print(seven_eleven(11) == 7)
#   print(seven_eleven(12) == 18)
#   print(seven_eleven(25) == 75)
#   print(seven_eleven(100) == 1153)
#   print(seven_eleven(0) == 0)
#   print(seven_eleven(-100) == 0)
# Data Structure and Algorithm:
#   - If argument number is less than 0, return 0
#   - Initialize current_num to 7
#   - Intialize multiples to empty set
#   - while current_num is less than argument number
#       - if current_num is multiple of 7 or 11
#           - add it to multiples
#       - Increase current_num value by 1
#   - Return sum of multiples

def seven_eleven(number):
    if number < 0:
        return 0

    current_num = 7
    multiples = set()
    while current_num < number:
        if (current_num % 7 == 0) or (current_num % 11 == 0):
            multiples.add(current_num)
        current_num += 1
    
    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)