# input: list of numbers
# output: new list of numbers
# rules:
#   Explicit:
#       - Returns a list of numbers with consecutive duplicate numbers
#         removed.
#       - Retain only the initial occurence
# Test Cases / Examples:
#   original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
#   expected = [1, 2, 6, 5, 3, 4]
#   print(unique_sequence(original) == expected)      # True

#   # Non-consecutive duplicates are kept
#   original = [1, 2, 1, 3]
#   expected = [1, 2, 1, 3]
#   print(unique_sequence(original) == expected)      # True
# Data Structure and Algorithm:
#   - If length of the original list is 0
#       - Return empty list
#   - Initialize variable 'refined_numbers' to list conating first 
#     num of original list to refined_list
#   - Iterate from second number to last number in original list:
#       - If number is not equal to last number of refined_list
#           add number to refined_list
#   - Return refined_list

def unique_sequence(numbers):
    if not numbers:
        return []

    refined_numbers = [numbers[0]]
    for num in numbers[1:]:
        if num != refined_numbers[-1]:
            refined_numbers.append(num)
    
    return refined_numbers

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True
