# input: Integer
# output: Boolean True or False
# rules:
#   - Return True it is prime number, otherwise False
#   - Prime number is a positive number that is evenly divisible
#     only by itself and 1. Thus 23 is a prime number. Its only divisors
#     are 1 and 23.
#   - Number 1 is not a prime.
#   - The number will always be positive.
# Test Cases / Examples
#   print(is_prime(1) == False)              # True
#   print(is_prime(2) == True)               # True
#   print(is_prime(3) == True)               # True
#   print(is_prime(4) == False)              # True
#   print(is_prime(5) == True)               # True
#   print(is_prime(6) == False)              # True
#   print(is_prime(7) == True)               # True
#   print(is_prime(8) == False)              # True
#   print(is_prime(9) == False)              # True
#   print(is_prime(10) == False)             # True
#   print(is_prime(23) == True)              # True
#   print(is_prime(24) == False)             # True
#   print(is_prime(997) == True)             # True
#   print(is_prime(998) == False)            # True
#   print(is_prime(3_297_061) == True)       # True
#   print(is_prime(23_297_061) == False)     # True
# Data Structure and Algorithm:
#   - If number is 1
#       - return False
#   - Iterate from number 2 to number less than 1: call it divisor
#       - if number % divisor == 0:
#           - return False
#   - Return True

def is_prime(num):
    if num == 1:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True