def calculate_average(*numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average())