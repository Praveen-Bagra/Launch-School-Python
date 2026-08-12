# numbers = [1, 2, 3, 4, 5]
# even_numbers = []

# for number in numbers:
    # if number % 2 == 0:
        # even_numbers.append(number)

# print(even_numbers)

# def even(number):
    # return number % 2 == 0

# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(even, numbers)
# print(list(even_numbers))

numbers = [1, 2, 3, 4, 5]
transformed_numbers = [number**2 for number in numbers]
print(transformed_numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = [number
                for number in numbers
                if number % 2 == 0]
print(even_numbers)