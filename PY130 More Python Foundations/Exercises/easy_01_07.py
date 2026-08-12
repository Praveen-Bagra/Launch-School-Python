nested_numbers_lst = [[1, 2], [3], [4, 5, 6], [7, 8]]
flat_numbers = list(num for inner_list in nested_numbers_lst
                        for num in inner_list)
print(flat_numbers)