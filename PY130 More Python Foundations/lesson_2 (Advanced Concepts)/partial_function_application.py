def add(x, y):
    return x + y

def make_adder(x):
    def adder(y):
        return add(x, y)

    return adder

add1 = make_adder(1)
add2 = make_adder(2)
add100 = make_adder(100)

print(add1)
print(add1.__closure__)

print(add1(10))
print(add2(10))
print(add100(10))
