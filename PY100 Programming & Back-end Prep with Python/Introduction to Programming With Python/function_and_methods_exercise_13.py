def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
# the function definition will raise an error. parameter without default value
# cannot follow parameter with default value.