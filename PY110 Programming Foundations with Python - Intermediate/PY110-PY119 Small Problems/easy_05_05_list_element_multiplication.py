def multiply_items(lst_a, lst_b):
    # new_list = []
    # for idx in range(len(lst_a)):
        # new_list.append(lst_a[idx] * lst_b[idx])

    # return new_list
    # return [lst_a[idx] * lst_b[idx] for idx in range(len(lst_a))]
    return [num1 * num2 for num1, num2 in zip(lst_a, lst_b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True