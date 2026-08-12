def my_filter(callback, iterable):
    result = []
    for element in iterable:
        if callback(element):
            result.append(element)

    return result

def even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = my_filter(even, numbers)
print(even_numbers)
