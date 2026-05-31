def merge_sets(lst1, lst2):
    # return set(lst1 + lst2)

    #   new_set = set()
    #   for element in lst1:
        #   new_set.add(element)

    #   for element in lst2:
        #   new_set.add(element)
        
    #   return new_set
    # return set(lst1) | set(lst2)
    return set(lst1).union(set(lst2))



list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True