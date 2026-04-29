def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner2:", x)
    
    inner_func1()
    inner_func2()

my_func()
# It will print:
# Inner 1:, 25
# Inner 2: 15 # Since functions have local scope, it can't access
#               x's value from func 1 and also since x is not initialized
#               in func2, it will search for nearest definition of x and
#               that is in my_fuct. It will print accordingly.