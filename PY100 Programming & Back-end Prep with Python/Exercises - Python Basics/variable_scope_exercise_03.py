def my_function():
    a = 1

    if True:
        print(a)

my_function()

# From line 1 to line 5, there is function definition.
# On line 7, we are invoking function my_fuction() and it will print
# 1 since in conditional expression in function definition, True is 
# truthy and will execute the if block that contains print statement.

# variables initalized inside the same scope whree a block begins can 
# be accessed inside the block.