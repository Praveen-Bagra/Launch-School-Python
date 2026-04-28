# input: number
# output: Returns number. Returns number multiplied by 2 if it not a 
#         double number, if doulbe number return as it is.
#         Double number is a number who is even and whose left side 
#         numbers are exactly same as right side numbers. For example
#         44, 334334, 103103 are double numbers whereas 444, 334433 are
#         not even numbers.
# Test Cases:
#   print(twice(37) == 74)                  # True
#   print(twice(44) == 44)                  # True
#   print(twice(334433) == 668866)          # True
#   print(twice(444) == 888)                # True
#   print(twice(107) == 214)                # True
#   print(twice(103103) == 103103)          # True
#   print(twice(3333) == 3333)              # True
#   print(twice(7676) == 7676)              # True
# Data Structure and Algorithm:
#   a. initialize str_number = str(number)
#   b. Check the length for str_number:
#           if odd return number * 2
#      else
#           half length = str length divided by 2
#           check_index = half length
#           iterate over the half characters
#               Check first character and appropriate character
#               check second character and appropriate character
#               and so on...
#               If any of them is not equal
#                   return number * 2
#   c. Return number

def twice(number):
    str_number = str(number)
    if len(str_number) % 2 == 1:
        return number * 2
    else:
        half_length = len(str_number) // 2
        check_index = half_length 
        for idx in range(half_length):
            if str_number[idx] != str_number[check_index]:
                return number * 2
            check_index += 1 
    return number

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
