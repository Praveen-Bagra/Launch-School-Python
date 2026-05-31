# input: list
# output: same list
# rules:
#   Explicit:
#       - Return the orignal list with its elements reversed.
#       - Not use list.reverse mehtod or slice ([::-1])
#   Implicit:
#       - Returns a empty list when original list is empty.
# Test Cases / Examples:
#   list1 = [1, 2, 3, 4]
#   result = reverse_list(list1)
#   print(result == [4, 3, 2, 1])               # True
#   print(list1 is result)                      # True

#   list2 = ["a", "b", "c", "d", "e"]
#   result2 = reverse_list(list2)
#   print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
#   print(list2 is result2)                     # True

#   list3 = ["abc"]
#   result3 = reverse_list(list3)
#   print(result3 == ['abc'])                   # True
#   print(list3 is result3)                     # True

#   list4 = []
#   result4 = reverse_list(list4)
#   print(result4 == [])                        # True
#   print(list4 is result4)                     # True
# Data Structure and Algorithm:
#   - Initialize dup to:
#     copy the list
#   - Initialize idx to -1
#   - Iterate over each element in dup list:
#       - original list [idx] = element
#       - Decrease idx value by 1
#   -return original list

def reverse_list(lst):
    #   dup = lst.copy()
    #   idx = -1
    #   for element in dup:
        #   lst[idx] = element
        #   idx -= 1

    #   return lst

    first = 0
    last = -1

    for _ in range(len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True


list5 = [1, 2]
result5 = reverse_list(list5)
print(result5 == [2, 1])                    # True
print(list5 is result5)                     # True