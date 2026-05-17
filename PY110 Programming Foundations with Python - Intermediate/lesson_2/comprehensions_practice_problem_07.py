lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# def multiple_of_3_list(my_lst):
    # return [num for num in my_lst if num % 3 == 0]

# multiple_of_3 = [multiple_of_3_list(sub_lst) for sub_lst in lst]
# print(multiple_of_3)


# multiple_of_3 = [[num for num in sub_lst if num % 3 == 0]
                      # for sub_lst in lst]

# print(multiple_of_3)

# new_list = []

# for sub_lst in lst:
    # new_sub_list = []
    # for num in sub_lst:
        # if num % 3 == 0:
            # new_sub_list.append(num)

    # new_list.append(new_sub_list)

# print(new_list)

new_list = []

for sub_lst in lst:
    new_sub_list = [num for num in sub_lst if num % 3 == 0]
    new_list.append(new_sub_list)

print(new_list)