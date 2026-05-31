# input: 2 lists containing numbers
# output: list
# rules:
#   Explicit:
#       - Returns a new list containing the product of each pair of
#         of numbers from the arguments lists that have the same index.
#       - The arguments lists will contain the same number of elements.
# Test Cases / Examples:
#   list1 = [3, 5, 7]
#   list2 = [9, 10, 11]
#   print(multiply_list(list1, list2) == [27, 50, 77])  # True
# Data Structure and Algorithm:
#   - Initialize product_lst to empty list.
#   - Iterate over no of times (from 1 to length of any list)
#       - product = original first lst element * 
#                 original second list second element
#       - add product to product_lst
#   - Return product_lst

def multiply_list(lst1, lst2):
    # product_lst = []
    # for idx in range(len(lst1)):
        # product = lst1[idx] * lst2[idx]
        # product_lst.append(product)

    # return product_lst
    return [a * b for a, b in zip(lst1, lst2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

