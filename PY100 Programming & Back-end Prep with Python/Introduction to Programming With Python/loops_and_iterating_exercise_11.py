my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

outer_list_index = 0

while outer_list_index < len(my_list):
    nested_list_index = 0
    while nested_list_index < len(my_list[outer_list_index]):
        number = my_list[outer_list_index][nested_list_index]
        if number % 2 == 0:
            print(number)

        nested_list_index += 1

    outer_list_index += 1
    