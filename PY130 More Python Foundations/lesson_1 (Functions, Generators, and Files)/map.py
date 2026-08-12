numbers = [1, 2, 3, 4, 5]
# transformed_numbers = []

# for number in numbers:
    # square = number**2
    # transformed_numbers.append(square)

# print(transformed_numbers)

def square(number):
    return number**2

numbers = [1, 2, 3, 4, 5]
transformed_numbers = map(square, numbers)
print(list(transformed_numbers))