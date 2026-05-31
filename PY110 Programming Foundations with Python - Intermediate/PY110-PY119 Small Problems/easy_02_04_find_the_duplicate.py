# input: list
# output: integer
# rules:
#   Explicit:
#       - To return a value which is duplicate in the original list.
#       - Exactly one value will be duplicate in the orginal lsit. 
#         Other values will be unique.
# Test Cases / Examples:
#    print(find_dup([1, 5, 3, 1]) == 1) # True
# Data Structure and Algorithm:
#   - Iterate over each num in the list
#       if count of any num is 2 in the list:
#           return num

def find_dup(lst):
    for num in lst:
        if lst.count(num) == 2:
            return num

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True