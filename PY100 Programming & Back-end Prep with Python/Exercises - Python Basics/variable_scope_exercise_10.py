b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function() # We cannot reassign b unless we add a keyword global
              # or initialze it in fuction definition. However we can
              # alter/reassign list elements
              
print(b) # Prints [10, 2, 3]