# input: Integer
# output: Integer
# rules:
#   - Explicit:
#       - Returns the index of first Fibonacci number that has the 
#         number of digits speicied by the argument.
#       - The first Fibonacci number has an index of 1
#       - The argument is always an integer greater than equal to
#         2.
# Test Cases / Examples:
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
#   print(find_fibonacci_index_by_length(2) == 7)
#   print(find_fibonacci_index_by_length(3) == 12)
#   print(find_fibonacci_index_by_length(10) == 45)
#   print(find_fibonacci_index_by_length(16) == 74)
#   print(find_fibonacci_index_by_length(100) == 476)
#   print(find_fibonacci_index_by_length(1000) == 4782)

#   # Next example might take a little while on older systems
#   print(find_fibonacci_index_by_length(10000) == 47847)
# Data Structure and Algorithm:
#   - Initialize variable 'idx' to 2
#   - Initialize fibonacci_series to [1, 1]
#   - while True:
#       - fibonacci_number = fibonacci series last element + fibonacci series second last element
#       - add fibonacci_number to fibonacci_series
#       - Increase idx value by 1
#       - Remove fibonacci series first element to improve performance.
#       - If last element of the fibonacci series has same length as 
#         specified by the argument
#           - break
#   - Return idx

import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    idx = 2
    fibonacci_series = [1, 1]
    while True:
        fibonacci_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(fibonacci_number)
        idx += 1
        fibonacci_series.pop(0)

        if len(str(fibonacci_series[-1])) == length:
            break

    return idx

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
