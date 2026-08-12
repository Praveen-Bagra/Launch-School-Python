# adders = []
# for n in range(1, 4):
    # adders.append(lambda x, addend=n: addend + x)

# print(adders)
# add1, add2, add3 = adders
# print(add1(10))
# print(add2(10))
# print(add3(10))


# adders = []
# for n in range(1, 4):
    # def create_adder(x):
        # return x + n

    # adders.append(create_adder)

# print(adders)

# print(adders[0](1))

# adders = []
# for n in range(1, 4):
    # def create_adder(x, addend=n):
        # return x + addend

    # adders.append(create_adder)

# print(adders[0](1))

# def adder(n, z):
    # def add(x):
        # return n + x + z

    # return add

# # add1, add2, add3 = [adder(n) for n in range(1, 4)]
# add3 = adder(1, 2)
# print(add3.__closure__)
# print(add3(2))