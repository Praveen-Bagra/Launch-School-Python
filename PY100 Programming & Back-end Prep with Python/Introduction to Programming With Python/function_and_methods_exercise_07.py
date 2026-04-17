def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')
# It will raise an error. Missing Argument . We have defined the function with
# two parameters with no default values for either. However we are passing 
# only one argument, so it will raise an error.