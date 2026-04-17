a = 1

def my_function():
    global a
    a = 2

my_function() # By adding global a statement in fuction definition, 
              # now we are reassigning global variable a to 2 
print(a) # Prints 2