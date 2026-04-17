set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# It would print {42, 'Monty Python', ('a', 'b', 'c'), 5, 6, 7, 8, 9}
# Not in the exact order since it is a set. Range is a lazy sequence. It would
# print range object and not individual values. 