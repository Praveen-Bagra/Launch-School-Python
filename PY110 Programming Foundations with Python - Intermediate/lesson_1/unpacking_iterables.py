# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# joined_numbers = numbers1 + numbers2
# print(joined_numbers)

# tup1 = ('a', 'b')
# tup2 = ('c', 'd')
# joined_tup = tup1 + tup2
# print(joined_tup)

# numbers = [1 ,2 ,3, 4]
# tup1 = (5, 6)
# tup2 = (7, 8)
# # joined_iterables = numbers + tup1 + tup2
# joined_iterables = numbers + list(tup1) + list(tup2)
# print(joined_iterables)

# numbers = [1 ,2 ,3, 4]
# tup1 = (5, 6)
# tup2 = (7, 8)
# joined_list = [*numbers, *tup1, *tup2]
# print(joined_list)


# numbers = [1 ,2 ,3, 4]
# tup1 = (5, 6)
# tup2 = (7, 8)
# joined_tuple = (*numbers, *tup1, *tup2)
# print(joined_tuple)

# joined_set = {*numbers, *tup1, *tup2}
# print(joined_set)

# def test(num1, num2, num3):
    # return num1 + num2 + num3

# num = [1, 2, 3]
# print(test(num[0], num[1], num[2]))
# print(test(*num))

# numbers = [1, [2, 3, 4], 5]
# a, (b, c, d), e = numbers
# print(a, b, c, d, e)

# numbers = [1, 1, 2, 3, 3, 4, 5, 5]
# set_nums = {*numbers}
# print(set_nums)

# numbers = [1, 1, 2, 3, 3, 4, 5, 5]
# set_nums = set(numbers)
# print(set_nums)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'd': 4}
merged_dict1 = {**dict1, **dict2}
print(merged_dict1)