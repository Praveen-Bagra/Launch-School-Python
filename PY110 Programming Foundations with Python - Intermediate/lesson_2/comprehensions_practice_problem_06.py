lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# updated_lst = [ {key: sub_dict[key] + 1}
                # for sub_dict in lst
                # for key in sub_dict ]
updated_lst = [{key: value + 1 for key, value in sub_dict.items()}
                               for sub_dict in lst]

print(updated_lst)
print(lst)