def remainders_3(numbers):
    result = []
    for number in numbers:
        result += [number % 3]
    return result

def any_non_divisible_by_3(remainders_by_3):
    return any(remainders_3(remainders_by_3))

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any_non_divisible_by_3(numbers_1))
print(any_non_divisible_by_3(numbers_2))
print(any_non_divisible_by_3(numbers_3))
print(any_non_divisible_by_3(numbers_4))
