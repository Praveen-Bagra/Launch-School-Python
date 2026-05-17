# numbers = [1, 3, 9, 11, 1, 4, 1]
# ones = []

# for current_num in numbers:
    # if current_num == 1:
        # ones.append(current_num)

# print(ones)

# fruits = ['apple', 'banana', 'pear']
# transformed_elements = []

# for current_element in fruits:
    # transformed_elements.append(current_element + 's')
    
# print(transformed_elements)

# def select_vowels(s):
    # selected_chars = ''

    # for char in s:
        # if char in 'aeiouAEIOU':
            # selected_chars += char

        # return selected_chars

# phrase = 'the quick brown fox'
# print(select_vowels(phrase))

# sentence = 'I wandered lonely as a cloud'
# print(select_vowels(sentence))
# print(sentence)

# number_of_vowels = len(select_vowels('hello world'))
# print(number_of_vowels)

# produce = {
    # 'apple': 'Fruit',
    # 'carrot': 'Vegetable',
    # 'pear': 'Fruit',
    # 'broccoli': 'Vegetable'
# }

# def select_fruit(my_dict):
    # selected_fruits = {}
    # for current_key, current_value in my_dict.items():
        # if current_value == 'Fruit':
            # selected_fruits[current_key] = current_value
    
    # return selected_fruits

# print(select_fruit(produce))

# def double_numbers(numbers):
    # double_nums = []

    # for current_num in numbers:
        # double_nums.append(current_num * 2)

    # return double_nums

# def double_numbers(numbers):
    # idx = 0
    # for _ in numbers:
        # numbers[idx] *= 2
        # idx += 1   

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(my_numbers)
# double_numbers(my_numbers)
# print(my_numbers)

# def double_odd_numbers(numbers):
    # doubled_nums = []

    # for current_num in numbers:
        # if current_num % 2 == 1:
            # doubled_nums.append(current_num * 2)
        # else:
            # doubled_nums.append(current_num)
    
    # return doubled_nums

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_odd_numbers(my_numbers))

# def double_old_indexes(lst):
    # double_old_idxes = []

    # for current_idx, current_num in enumerate(lst):
        # if current_idx % 2 == 1:
            # double_old_idxes.append(current_num * 2)
        # else:
            # double_old_idxes.append(current_num)

    # return double_old_idxes

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_old_indexes(my_numbers))

# def select_type(produce_list, selection_criterion):
    # selected_items = {}

    # for current_key, current_value in produce_list.items():
        # if current_value == selection_criterion:
            # selected_items[current_key] = current_value

    # return selected_items

# produce = {
    # 'apple': 'Fruit',
    # 'carrot': 'Vegetable',
    # 'pear': 'Fruit',
    # 'broccoli': 'Vegetable',
# }

# print(select_type(produce, 'Fruit'))
# print(select_type(produce, 'Vegetable'))
# print(select_type(produce, 'Meat'))

def multiply(nums_list, multiply_by_num):
    multiplied_list = []

    for current_num in nums_list:
        multiplied_list.append(current_num * multiply_by_num)

    return multiplied_list

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]