def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
# It will raise an error. We have defined the function with two parameters,
# however we are passing three aruguments at function call. 
# Expected two arguments, passed three. 
