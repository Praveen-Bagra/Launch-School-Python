from functools import partial

def add(x, y):
    return x + y

add1 = partial(add, 1)
print(add1(5))

add100 = partial(add, 100)
print(add100(5))