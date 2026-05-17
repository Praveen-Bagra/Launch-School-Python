a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

print(a) # Prints 2
print(b) # Prints [3, 8]
print(lst) # Prints [4, [3, 8]]