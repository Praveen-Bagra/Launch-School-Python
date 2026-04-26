# input: number
# output: Return number. If is is positive, return the negatgive of that
#         number. If it is negative, return the same number.
# Test Cases:
#   print(negative(5) == -5)      # True
#   print(negative(-3) == -3)     # True
#   print(negative(0) == 0)       # True
# Data Structure and Algorithm:
#   a. Check the argument number, if is less than equal to 0:
#       return argument number
#      else:
#       return argument number * -1

def negative(number):
    if number <= 0:
        return number
    else:
        return number * -1

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True