a = 1

def my_function():
    a = 2

my_function() # Assigns local variable a to 2. This doesn't affect
              # global variable a. 
print(a) # Prints 1. Variables initiazlied inside the function
         # defintion cannot be accessed outside. It referes to global
         # variable a.