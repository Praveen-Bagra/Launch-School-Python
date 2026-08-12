def reduce(callback, iterable, starting_value):
    accum = starting_value
    for item in iterable:
        accum = callback(item, accum)

    return accum

numbers = [1, 2, 3, 4, 5]
total_of_squares = lambda number, accum: accum + number**2
print(reduce(total_of_squares, numbers, 0))
