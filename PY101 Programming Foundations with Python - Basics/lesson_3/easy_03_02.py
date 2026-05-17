import operator

print([1, 2, 3] + [4, 5])
# It will print [1, 2, 3, 4, 5]

a = [1, 2, 3, 4]
b = [5, 6, 7]

c = operator.concat(a,b)
print(c)