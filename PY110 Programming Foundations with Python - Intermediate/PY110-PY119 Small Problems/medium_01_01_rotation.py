# input: list
# ouput: new list
# rules:
#   Explicit:
#       - Returns a new list by moving the first element to the end of the
#         list. The elements should rotate in the new list.
#         First element will be last, second element will be first,
#         third element will be second and so on...
#      - If the input is an empty list, return an empty list
#      - It input is not a list, return None
# Test Cases / Examples:
# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])
# Data Structure and Algorithm:
#   - It type of argument is not list
#       - return None
#   - If length of the original is less than equal to 1
#       - return all the elements of original list as new list.
#     else
#       - return list(from 2nd element to last) + list first element

def rotate_list(lst):
    # if type(lst).__name__ != 'list':
        # return None

    if not isinstance(lst, list):
        return None

    return lst[1:] + lst[:1] 

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])