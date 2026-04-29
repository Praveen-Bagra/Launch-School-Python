def my_func():
    num = 10

my_func()
print(num)
# It will raise NameError exception - 'num' is not defined.
# Functions have local scope. The variables initialized in an function
# cannot be accessed outside unless there is a keyword 'global' or
# 'nonlocal' in function definition.