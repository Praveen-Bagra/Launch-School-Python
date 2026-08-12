numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda num: num % 2 == 0, numbers))

# def is_even(num):
    # return num % 2 == 0

# even_numbers = list(filter(is_even, numbers))
print(even_numbers)