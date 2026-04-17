def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
# It will print:
# 42
# 3
# 2
# We've defined the function foo with three parameters having default values
# for the second and third parameter. We've passed one argument to the 
# function, so python passes default values as arguments to the function for 
# second and third parameter.  