def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer() 
# It will print Hello, World. Since we invoked outer() on line 10, the
# code inside the function outer() rusn and invokes function inner() on
# line 8. The code inside the function inner() executes and print
# Hello, World. Variable outer_var value is accessible inside the inner() 
# function due to lexical scope. And inner_var is already initialized in
# the same scope.
 