def set_foo(): # Defining the function here
    foo = 'bar' # Assigning a variable foo to the string ojbect 'bar'

set_foo() # We are calling a function 'set_foo'. This will execute the 
#           function body and return None.
print(foo) # It will raise an error. 'foo' not defined. Variable follow
#            function scope i.e. variable assigned in function is not available
#            outside the function.