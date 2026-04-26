# input: number greater than 1
# output: Returns number i.e. sum of all the unique numbers between 1 
#         and above number, inclusive, that are multiples of 3 or 5. 
# Test Cases:
#   multisum(20) # Returns 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20)
#   multisum(3)  # Returns 3
#   multipsum(8) # Returns 8 (3 + 5)
#   multisum(10) # Returns 33 (3 + 5 + 6 + 9 + 10)
#   multipsum(2) # Returns 0
# Data Stucture and Algorithm:
#   a. Initialize result = []
#   b. Iterate over range from 1 to argument number inclusive:
#       i. If is multiple of 3 or 5, append num to result 
#   c. Return the sum of the result.

def multisum(number):
    result = []
    for num in range(1, number + 1):
        if (num % 3 == 0) or (num % 5 == 0):
            result.append(num)

    return sum(result)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
print(multisum(2) == 0)

