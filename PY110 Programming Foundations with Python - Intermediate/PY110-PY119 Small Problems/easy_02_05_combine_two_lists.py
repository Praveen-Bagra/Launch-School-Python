def interleave(lst1, lst2):
    # new_list = list(zip(lst1, lst2))
    # result = [element for tup in new_list for element in tup]
    # return result


#    result = []
    #for idx, element in enumerate(lst1):
        #result.append(element)
        #result.append(lst2[idx])
    
    #return result

    # result = []
    # for idx in range(len(lst1)):
        # result.extend([lst1[idx], lst2[idx]])

    # return result

    result = []
    for idx in range(len(lst1)):
        result.append(lst1[idx])
        result.append(lst2[idx])

    return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2)  == expected)      # True