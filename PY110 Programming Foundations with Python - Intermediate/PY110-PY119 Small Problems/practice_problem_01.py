# input: list
# output: a new list
# rules
#   Explicit:
#       - Returns the list containing count of the numbers smaller
#   `     than the original number
#       - For the purpose of counting, only unique numbers should be
#         considered.
#   Implicit:
#       - The resulting list will contain same number of elements as 
#         in the original list.
# Test Cases / Examples:
#   print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
#   print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
#   print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
#   print(smaller_numbers_than_current([1]) == [0])

#   my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
#   result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
#   print(smaller_numbers_than_current(my_list) == result)
# Data Structure and Algorithm:
#   - Initialize varible smaller_than to empty list.
#   - Iterate for each num in original list:
#       - Initialize count = 0
#       - Iterate for each number in remaining_unique_numbers (num, my_list):
#           - if num is smaller than than current num
#               - increase count value by 1
#       - Add count to smaller_than
#   - Return smaller_than
# Helper Function remaining _unique_numbers
#   - Will convert list into set. It will remove the duplicates. Will
#     again convert into list
#   - Remove the num from list.
#   - Return the list.

def smaller_numbers_than_current(numbers):
    smaller_than = []
    for current_num in numbers:
        count = 0
        remaining_numbers = return_remaining_numbers(current_num, numbers)
        for num in remaining_numbers:
            if num < current_num:
                count += 1
        smaller_than.append(count)

    return smaller_than           

def return_remaining_numbers(current_num, numbers):
    numbers = list(set(numbers))
    numbers.remove(current_num)
    return numbers


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)



