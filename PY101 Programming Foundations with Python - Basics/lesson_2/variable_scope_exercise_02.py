num = 5

def my_func():
    num = 10

my_func()
print(num) # It will print 5. We are initializing a new local variable
           # on line 4 in my_func function. The variable num on line 1
           # and line 4 are seperate variables. They have no relation
           # between each other. And since function have local scope, 
           # the num on line 7 refrences the same object to which it 
           # was initialized. 