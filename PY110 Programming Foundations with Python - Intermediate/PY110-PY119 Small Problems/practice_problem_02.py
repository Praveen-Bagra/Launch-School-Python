# input: list
# output: Integer
# rules
#   Explicit
#       - It should return the minimum sum of 5 consecutive numbers
#         in the list.
#       - If the list contains fewer than 5 elements, the function should
#         return None
# Test Cases / Examples
#   print(minimum_sum([1, 2, 3, 4]) is None)
#   print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
#   print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
#   print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
#   print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
# Data Structure and Algorithm:
#   - Helper Function: return all possible five consecutive numbers in list.
#       It will return a list containing nested lists of possible consecutive numbers.
#   - If length of list is less than 5, return None
#   - Initialize possible_combinations = return value of helping function. 
#   - I will initialize variable sum to first element sum in possible combinations.
#   - I will iterate each list in possible combinations:
#       - Check the sum of each list, if is less than sum than reassin sum to that value
#   - Return sum

# Helper Function:
# input: list containing numbers
# output : list contaiing lists of numbers
#   - I will initialize `starting_idx` to 0
#   - I will initialize possible_combinations_lst to empty list.
#   - while staring_idx + 5 is less than equal to length of the list:
#       - Add list[starting_idx: starting_idx + 5] to possbile_combinations_lst
#       - Increase starting_idx value by 1 
#   - Return possible_combinations_lst

def return_possible_combinations(numbers):
    starting_idx = 0
    possbile_combinations_lst = []
    while (starting_idx + 5) <= len(numbers):
        possbile_combinations_lst.append(numbers[starting_idx:starting_idx + 5])
        starting_idx += 1
    return possbile_combinations_lst

def minimum_sum(numbers):
    if len(numbers) < 5:
        return None

    possible_combinations = return_possible_combinations(numbers)
    total_sum = sum(possible_combinations[0])
    for sub_list in possible_combinations:
        if sum(sub_list) < total_sum:
            total_sum = sum(sub_list)
    
    return total_sum

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

