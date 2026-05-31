# input: 2 integers
# output: list
# rules:
#   Explicit:
#       - The first argument is the count.
#       - The second argument is the starting point as well as step.
#         The elements should be multiple of this second argument.
#       - Count will be greater than or equal to 0. 
#       - The starting integer can be any integer.
#       - If the count is 0, the function should return  
# Test Cases / Examples:
#   print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
#   print(sequence(4, -7) == [-7, -14, -21, -28])     # True
#   print(sequence(3, 0) == [0, 0, 0])                # True
#   print(sequence(0, 1000000) == [])                 # True
# Data Structure and Algorithm:
#   - If the count is 0:
#       return emtpy list
#   - Initialize variable result to empty list.
#   - Initialize elemment to starting_num
#   - Itetrate for num of count:
#       add element to result list.
#       increase element value by starting_num 
#   - Return result list.

def sequence(count, starting_num):
    # if count == 0:
        # return []
    
    # result = []
    # element = starting_num
    # for _ in range(count):
        # result.append(element)
        # element += starting_num

    # return result

    return [starting_num * num for num in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True