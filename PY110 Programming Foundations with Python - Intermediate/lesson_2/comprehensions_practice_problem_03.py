lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_lst = []
for inner_lst in lst:
    sorted_lst.append(sorted(inner_lst, key=str))

print(sorted_lst)

sorted_lst = [sorted(inner_lst, key=str) for inner_lst in lst]
print(sorted_lst)
print(lst)