foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo() # It is calling a function set_foo. Then it executes fuction body
#           and assignes variable foo to str object 'bar' and returns None.
print(foo) # It will output 'bar' in the console since "foo = 'qux'" in fuction
#            definition is not in the scope.