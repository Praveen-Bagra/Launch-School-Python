def reduce(callback, iterable, starting_value):
    # for idx, item in enumerate(iterable):
        # if idx == 0:
            # accum = callback(item, starting_value)
        # else:
            # accum = callback(item, accum)

    # return accum

    accum = starting_value
    for item in iterable:
        accum = callback(item, accum)

    return accum

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))     # 300

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV