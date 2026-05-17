lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_key(sub_lst):
    return sum([num for num in sub_lst if num % 2 == 1])

sorted_lst = sorted(lst, key=odd_key)
print(sorted_lst)

# sorted_lst = sorted(lst, key=sum([num for sub_lst in lst
#                                      for num in sub_lst
#                                      if num % 2 == 1]))
