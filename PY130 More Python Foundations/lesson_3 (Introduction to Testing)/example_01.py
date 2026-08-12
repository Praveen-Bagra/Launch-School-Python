# num = 5
# print(isinstance(num, int))

# def add(a, b):
    # return a + b

# print(add(3, 4) == 7)
# print(add(4, 5) == 9)

def add(a, b):
    return a + b

assert add(3, 4) == 7, "Add function failed" # Equality Assertion

is_active = True
assert is_active, "Boolean check failed" # Boolean Assertion

def get_max(a, b):
    return max(a, b)

assert get_max(10, 20) > 15, "Comparison check failed" # Comparison Assertion

numbers = [1, 2, 3]
assert 2 in numbers, "Containment check failed" # Containment Assertion

try:
    x = 1 / 0
    assert False, "Exception check failed, no exception raised"
except ZeroDivisionError:
    pass