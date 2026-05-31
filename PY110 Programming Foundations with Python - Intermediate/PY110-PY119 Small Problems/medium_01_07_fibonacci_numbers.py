# input: Integer
# output: Integer
# rules:
#   Explicit:
#       - Returs the fibonacci number as per integer value passed as 
#         an argument.
#       - Fibonacci series is a sequence of numbers in which each
#         number is the sum of the previous two numbers.
#       - The first two numbers are 1 and 1.
#       - So the series will look like [1, 1, 2, 3, 5...]
# Test Cases / Examples:
#   print(fibonacci(1) == 1)                  # True
#   print(fibonacci(2) == 1)                  # True
#   print(fibonacci(3) == 2)                  # True
#   print(fibonacci(4) == 3)                  # True
#   print(fibonacci(5) == 5)                  # True
#   print(fibonacci(6) == 8)                  # True
#   print(fibonacci(12) == 144)               # True
#   print(fibonacci(20) == 6765)              # True
#   print(fibonacci(50) == 12586269025)       # True
#   print(fibonacci(75) == 2111485077978050)  # True
# Data Structure and Algorithm:
#   - If num is either 1 or 2
#       return 1
#   - Initialize variable 'fibonacci_series' to list containing:
#     [1, 1] 
#   - Iterate from 3 to number inclusive
#       fibonacci_number = fibonacci last elment + fibonacci second last element
#       add fibonacci_number to fibonacci_series
#   - Return last element(number) from fibonacci series.

def fibonacci(num):
    if num in [1, 2]:
        return 1
    fibonacci_series = [1, 1]
    for _ in range(3, num + 1):
        fibonacci_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(fibonacci_number)
    
    return fibonacci_series[-1]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True