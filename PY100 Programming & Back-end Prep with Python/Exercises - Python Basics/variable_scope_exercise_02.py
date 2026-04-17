x = 10

def my_function():
    x = x + 5
    print(x)

my_function() # Prints 15
print(x) # Prints 10. Variables intialized in function definition are
         # not accessible outside the fuction unless we use the keyword
         # global or nonlocal

# We have initliazed the global variable x to 10 on line 1
# We have defined the function my_fuction on lines 3 to 5
# On line 4, we are reassigning a new local variable (local to function),
# x to x + 5. Since we have not intialized x in functin, it will raise
# an error
# On line 7, we are invoking the function my_function() 