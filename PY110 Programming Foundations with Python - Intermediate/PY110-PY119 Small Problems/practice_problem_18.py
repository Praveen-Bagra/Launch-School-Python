# input: list
# output: Integer
# rules:
#   Explicit:
#       - Return the index n for which all numbers with an indes less
#         than n sum to the same value as the numbers and an index
#         greater than n
#       - If there is no index that would make this happend, return -1
#       - If you are given a list with multiple answers, return the
#         the index with the smallest value.
# Test Cases / Examples:
#   print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
#   print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
#   print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
#   print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

#   # The following test case could return 0 or 3. Since we're
#   # supposed to return the smallest correct index, the correct
#   # return value is 0.
#   print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
# Data Structure and Algorithm:
#   - Initialize combinations to all_combinations(list)  - HELPER
#   - Iterate over each sublist with idx in list :
#       - if idx is 0 or last index:
#           then check if sublist 1st element sum is 0:
#               return idx
#       - if sum of sublist 1st element and sum of sublist second element is 0:
#               return idx
#       - Return -1

# Helper function 
# input: list
# output: all possible combinations
#   - Initialize combinations to empty list.
#   - Initialize first_idx to 0
#   - while first_idx is less than less length of the list
#       - initialize sub_list to empty list
#       - initialize second_idx to = first_idx + 1
#       - add list[:firs_idx] to sublist
#       - add list[second_idx:] to sublist
#       - add sublist to combinations
#       = increase first_idx value by 1
#   - Return combinations

def all_combinations(lst):
    combinations = []
    idx = 0
    while idx < len(lst):
        sub_list = []
        sub_list.append(lst[:idx])
        sub_list.append(lst[idx + 1:])
        combinations.append(sub_list)
        idx += 1

    return combinations

print(all_combinations([1, 2, 4, 4, 2, 3, 2]))

def equal_sum_index(lst):
    combinations = all_combinations(lst)
    for idx, sublist in enumerate(combinations):
        if sum(sublist[0]) == sum(sublist[1]):
            return idx

    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

