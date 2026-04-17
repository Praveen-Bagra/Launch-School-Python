# numbers = [2, 5, 8, 10, 13]
# numbers = [5, 13]
numbers = [2, 8, 10]
result = []
for number in numbers:
    result += [number % 2 == 0]

print(any(result))
print(all(result))
