# input = 2 lists
# output = a list containing two elements which are lists
# rules
#   Explicit:
#       - Return a list containing two elements, which are also lists.
#       - First half of the original list items should in first element list.
#       - Second half of the original list items should be in the 
#         second element list
#       - If original list contains odd number of elements, the middle
#         element should be in first half
#   Implicit:
#       - If the original list contains 1 element, it should in the
#         first element list and second element list should be empty.
#       - If empty list is passed, the return list should contain
#         two empty lists.
# Test Cases / Examples
#   print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
#   print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
#   print(halvsies([5]) == [[5], []])
#   print(halvsies([]) == [[], []])
# Data Structure and Algorithm:
#   - half_length = length of the orignal lsit / 2 
#   - if original list has odd number of elements
#       half_length += 1
#   - first_half = orignal string 1st element to half length. 
#   - second_half = original string half_length elements to
#                           last element 
#           
#   return list contain first_half and second_half lists.

def halvsies(lst):
    half_length = len(lst) // 2
    if len(lst) % 2 == 1:
        half_length += 1

    first_half = lst[:half_length]
    second_half = lst[half_length:]

    return [first_half, second_half]
    
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])