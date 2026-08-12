from functools import reduce
numbers = [1, 2, 3, 4, 5]

def reduce1(callback, iterable, starting_value):
    for idx, num in enumerate(iterable):
        if idx == 0:
            accum = callback(num, starting_value)
        else:
            accum = callback(num, accum)

    return accum
        
def product(num, accum):
    return accum * num
    

print(reduce1(product, numbers, 1))
print(reduce1(lambda num, accum: num * accum, numbers, 1))

print(reduce(lambda num, accum: num * accum, numbers, 1))
print(reduce(product, numbers, 1))


