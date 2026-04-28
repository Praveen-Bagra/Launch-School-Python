# a function that takes two lists of numbers and returns the result of 
# merging the lists. The elements of the first list should become the 
# elements at the even indexes of the returned list, while the elements 
# of the second list should become the elements at the odd indexes. For
# instance:
# merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]

# START

# Gtiven the two lists of numbers

# SET total_elements_count = count of elments of lst1 & list 2
# SET result = []
# FOR loop. Iterate over range(total_elements_count)
#       append 0 to result 
#
# SET result_idx = 0
# SET list_idx = 0.0
# WHILE result_idx < length of result 
#       IF idx is even
#           SET result[result_idx] = lst1[int(list_idx)]
#       ELSE
#           SET result[result_idx] = lst2[int(list_idx)]
#       result_idx += 1
#       list_idx = list_idx + 0.5
# RETURN result

def merge(lst1, lst2):
    total_elements_count = len(lst1) + len(lst2)
    result = []
    for _ in range(total_elements_count):
        result.append(0)

    result_idx = 0
    list_idx = 0.0
    while result_idx < len(result):
        if result_idx % 2 == 0:
            result[result_idx] = lst1[int(list_idx)]
        else:
            result[result_idx] = lst2[int(list_idx)]
        result_idx += 1
        list_idx += 0.5

    return result

print(merge([1, 2, 3], [4, 5, 6]))
