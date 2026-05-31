# input: list
# output: Integer
#   rules:
#       - Returns the number of identical pairs of integers in the
#         original list.
#       - If list is empty of contains exactly one value, return 0
# Test Cases / Examples
#   print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
#   print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
#   print(pairs([]) == 0)
#   print(pairs([23]) == 0)
#   print(pairs([997, 997]) == 1)
#   print(pairs([32, 32, 32]) == 1)
#   print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
# Data Structure and Algorithm:
#   - Initialize unique_numbers to:
#     convert original list into set and again convert it into list
#   - Intialize total_pairs to 0
#   - Iterate for each num in unique_values
#       - Intialize count = count of numbers in the original list
#       - If count is greater than 1:
#           - num_pair = count // 2
#           - Increase total_pairs value by num_pair
#   - Return total_pairs

def pairs(numbers):
    unique_numbers = list(set(numbers))
    total_pairs = 0
    for unique_num in unique_numbers:
        unique_num_count = numbers.count(unique_num)
        if unique_num_count > 1:
            unique_num_pairs = unique_num_count // 2
            total_pairs += unique_num_pairs
    
    return total_pairs

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)