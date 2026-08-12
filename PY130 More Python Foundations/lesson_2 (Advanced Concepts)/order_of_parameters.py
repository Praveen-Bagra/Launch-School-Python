def custom_func(x, y, *agrs):
    pass

custom_func(1, 2) # args points to an empty tuple
custom_func(1, 2, 3, 4, 5) # agrs points to a tuple(3, 4, 5)
custom_func(1) # raises a TypeError

def custom_func(x, *args, y):
    pass
    
custom_func(1, 2, y=3) # args points to a a tuple(2)
custom_func(1, 2, 3) # raises a TypeError

def custom_func(x, *args, y=None, **kwargs):
    pass

custom_func(1, 2, y=3, z= 4)

def custom_func(x, *args, y=None, **kwargs, z=None):
    pass

custom_func(1, 2, y=3, z=4)
# SyntaxError: arguments cannot follow var-keyword argument