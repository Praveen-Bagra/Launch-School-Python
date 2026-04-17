def find_index(my_list, value):
    if my_list.count(value) > 0:
        print(my_list.index(value))
    else:
        print('Value not found.')

numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
find_index(numbers, 3)
find_index(numbers, 7)