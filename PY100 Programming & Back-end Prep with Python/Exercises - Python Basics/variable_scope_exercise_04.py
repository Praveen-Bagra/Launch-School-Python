a = 1

def my_function():
    print(a)

my_function()

# Line 6, invoking my_function() will print a's value i.e. 1

# Variables intialized outside the scode can be accessed in function
# defintion however they cannot be altered or reassigned without adding
# global or nonlocal keyword. Unless initialzed in the same block,
# python will look for it's nearest defintion. 