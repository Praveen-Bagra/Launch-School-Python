# from functools import reduce

def reduce(callback, iterable, starting_value):
    for idx, element in enumerate(iterable):
        if idx == 0:
            accum = callback(starting_value, element)
        else:
            accum = callback(accum, element)

    return accum

strings = ['hi', 'how', 'are', 'you']
single_string = reduce(lambda accum, string: accum + string, strings, '')
print(single_string)