data_set = {1, 2, 3, 4, 5}

lst = []
for item in data_set:
    if item % 2 == 0:
        lst.append(item)

for num in lst:
    data_set.remove(num)

print(data_set)

# It will raise an error becuase we are modifying the set and iterating
# over the set at the same time. We are changing its size during iteration.

