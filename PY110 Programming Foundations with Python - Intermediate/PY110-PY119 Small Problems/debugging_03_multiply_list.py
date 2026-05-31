def multiply_list(lst):
    for idx, item in enumerate(lst):
        item *= 2
        lst[idx] = item

    return lst

    # return [num * 2 for num in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# We are multiplying the item by 2 but we not storing that value
# anywhere. Return value of this expression is ignored.
# It returns the same list with same elements.