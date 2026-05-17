# lst = [num for num in range(5)]
# print(lst)

# nums = [1, 2, 3, 4, 5]

# squared = []
# for num in nums:
    # squared.append(num**2)

# print(squared)

# nums = [1, 2, 3, 4, 5]
# squared = [num**2 for num in nums]
# print(squared)

# nums = [1, 2, 3, 4, 5]

# evens = []
# for num in nums:
    # if num % 2 == 0:
        # evens.append(num)

# print(evens)

# nums = [1, 2, 3, 4, 5]
# evens = [num for num in nums if num % 2 == 0]
# print(evens)

# evens = [num**2 for num in nums if num % 2 == 0]
# print(evens)

# nums = [1, 1, 2, 3, 4, 4, 5]
# distinct_squares = {num**2 for num in nums}
# print(distinct_squares)

# distinct_odd_squares = {num**2 for num in nums if num % 2 != 0}
# print(distinct_odd_squares)

# fruits = ['apple', 'banana', 'cherry']
# fruit_length = {fruit: len(fruit) for fruit in fruits}
# print(fruit_length)

# matrix = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9],
# ]

# flattened_matrix = []

# for row in matrix:
    # for cell in row:
        # flattened_matrix.append(cell)

# print(flattened_matrix)

# flattened_matrix = [cell for row in matrix
                         # for cell in row]
# print(flattened_matrix)

# nums = (1, 2, 3, 4, 5)
# squared = [num**2 for num in nums]
# print(squared)

# nums = range(1, 6)
# squared = {num**2 for num in nums}
# print(squared)

# nums = {1, 2, 3, 4, 5}
# squared = {num: num**2 for num in nums}
# print(squared)

# my_str = 'Launch School'
# lowercase = {char for char in my_str if char.islower()}
# lowercase = ''.join(lowercase)
# print(lowercase)

# nums = [1, 2, 3, 4, 5]
# values = [print(num) for num in nums if num % 2 == 1]
# print(values)

# nums = [1, 2, 3, 4, 5]
# for num in nums:
    # if num % 2 == 1:
        # print(num)

# string = 'hello'
# str_lst = [c for c in string]
# print(str_lst)

string = 'hello'
str_lst = list(string)
print(str_lst)