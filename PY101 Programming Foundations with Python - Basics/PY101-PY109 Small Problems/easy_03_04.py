# input: postive integer (number)
# output: Returns string of alternative 1 & 0 i.e. 1010.... The length
#         of the string should be equal to numbers. Always
#         starts at 1. 
# Test Cases:
#   print(stringy(6) == "101010")           # True
#   print(stringy(9) == "101010101")        # True
#   print(stringy(4) == "1010")             # True
#   print(stringy(7) == "1010101")          # True
# Data Structure and Algorithm:
#   a. initialize string = ''
#   b. Iterate over the range (string length):
#   c. If num is even, add 1 else add 0
#   d. Return the string

def stringy(length):
    string = ''
    for idx in range(length):
        if idx % 2 == 0:
            string += '1'
        else:
            string += '0'
    
    return string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True