class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name
    
# The Pizza object would create instance variable my_name, since it is 
# prefixed by self. in __init__ method.

print(vars(Fruit('orange')))
print(vars(Pizza('pepperoni')))