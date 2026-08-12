def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter()
print(increment_counter()) # Prints 1
print(increment_counter()) # Prints 1

increment_counter = make_counter()
print(increment_counter()) # Prints 1
print(increment_counter()) # Prints 1