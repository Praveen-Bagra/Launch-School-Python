# input: list of numbers
# output: Integer
# rules:
#   Explicit:
#       - Returns the sum of the sums of each leading subsequent in that
#         list.
#       - Original list will always contain atleast one number.
# Test Cases / Examples:
#   print(sum_of_sums([3, 5, 2]) == 21)               # True
#   # (3) + (3 + 5) + (3 + 5 + 2) --> 21

#   print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
#   # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

#   print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
#   # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

#   print(sum_of_sums([4]) == 4)                      # True
# Data Structure and Algorithm:
#   - Initialize variable totals to empty list.
#   - Initialize variable total to 0
#   - Iterate for each num in original list:
#       - Increase total value by num
#       - Add total to totals
#   - Return sum of the totals list.

def sum_of_sums(lst):
    totals = []
    total = 0
    for num in lst:
        total += num
        totals.append(total)
    
    return sum(totals)

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True