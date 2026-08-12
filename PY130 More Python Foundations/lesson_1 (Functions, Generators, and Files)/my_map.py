def my_map(callback, iterable):
    # result = []
    # for element in iterable:
        # result.append(callback(element))

    # return result
    return [callback(element) for element in iterable]

def square(num):
    return num**2

# numbers = [1, 2, 3, 4, 5]

# squares = my_map(square, numbers)
# print(squares)

def upper(string):
    return string.upper()

strings = ['cat', 'dog', 'bird', 'fish']
transformed_strings = my_map(upper, strings)
print(transformed_strings)