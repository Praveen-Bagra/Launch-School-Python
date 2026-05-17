lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def all_nums_even(numbers):
    for num in numbers:
        if num % 2 == 1:
            return False
    
    return True
    
new_lst = [element_dict
           for element_dict in lst
           if all([all_nums_even(num_list) for num_list in element_dict.values()])] 

print(new_lst)

new_lst = []

for inner_dict in lst:
    dict_even_elemnts_in_a_lst = []
    for num_list in inner_dict.values():
        dict_even_elemnts_in_a_lst.append(all_nums_even(num_list))

    add_element = True
    for bool_result in dict_even_elemnts_in_a_lst:
        if bool_result == False:
            add_element = False
            break
    
    if add_element == True:
        new_lst.append(inner_dict)

print(new_lst)

    
dictionary = {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]}
def all_even_nums_in_all_list(dictionary):
    for num_lst in dictionary.values():
        for num in num_lst:
            if num % 2 == 1:
                return False
    
    return True
        
new_lst = [sub_dict for sub_dict in lst
                    if all_even_nums_in_all_list(sub_dict)]
print(new_lst)

def all_even(dictionary):
    for num_list in dictionary.values():
        print([num % 2 == 0 for num in num_list])

all_even({'b': [2, 4, 6], 'c': [3, 6], 'd': [4]})