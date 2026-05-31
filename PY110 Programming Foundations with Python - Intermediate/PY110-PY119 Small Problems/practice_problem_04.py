# input: list of numbers
# output: a tuple containing 2 numbers
# rules:
#   Explicit:
#       - Return a tuple of two number that are closest together in value.
#         The difference should be minumum between these two numbers
#         in comparison to any other pair. 
#       - If there are multiple pairs that are equally close, return
#         the pair that occurs first in the list.
# Test Cases / Examples
#   print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
#   print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
#   print(closest_numbers([12, 22, 7, 17]) == (12, 7))
# Data Structure and Algorithm:
#   - Helper function: return_all_combinations(numbers)
#       It will return a list containing list of possible pairs.
#   - Initialize all_combinations = return_all_combinations(numbers)
#   - Initialize difference to difference between first pair in abs number
#   - Initialize over each sub_list in all_combinations:
#       Check the absolute difference between pair in each sub_list
#       If is less than difference
#           - reassign difference to pair absolute difference
#       
#   - Again iterate each sub_list ia all_combinations:
#       if pair abs difference is equal to difference
#           return that list as a tuple

#   - Helper Function - Return all combinations(numnbers)
#       - Initialize starding_idx to 0
#       - Initialize all_combinations_lst = []
#       - while starting_idx is less than length of the numbers
#           - Initialize ending_idx = starting_idx + 1
#           - while ending_idx is less that equal to length of the numbers
#               - add numbers[starting_idx: ending_idx] to all_combinations_lst 
#               - Increase ending_idx value by 1.
#           - Increases starting_idx value by 1
#       - Return all_combinations_lst

#   - Helper function - absolute_difference
#     difference = list 1st element - list second element
#     if difference is less than 0
#           return difference * -1
#     else
#           return difference

def closest_numbers(numbers):
    all_combinations = return_all_combinations(numbers)
    difference = absolute_difference(all_combinations[0])
    for pair in all_combinations:
        pair_difference = absolute_difference(pair)
        if pair_difference < difference:
            difference = pair_difference

    for pair in all_combinations:
        if absolute_difference(pair) == difference:
            return tuple(pair)

def return_all_combinations(numbers):
    first_idx = 0
    all_combinations_lst = []
    while first_idx < len(numbers):
        second_idx = first_idx + 1
        while second_idx < len(numbers):
            all_combinations_lst.append([numbers[first_idx]] + [numbers[second_idx]])
            
            second_idx += 1
        first_idx += 1
    
    return all_combinations_lst

def absolute_difference(lst):
    difference = lst[0] - lst[1]
    if difference < 0:
        return difference * -1
    else:
        return difference

# print(return_all_combinations([5, 25, 15, 11, 20]))

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

