numbers = [1, 2, 3, 4]
numbers[0] = numbers[0] + 1

print(numbers)

numbers[1] += 1
print(numbers)

for idx in range(2, 4):
    numbers[idx] += 1

print(numbers)

numbers[4] += 1