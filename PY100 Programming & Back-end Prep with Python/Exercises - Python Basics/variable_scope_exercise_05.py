a = 1

def my_function():
    print(a)
    a = 2

my_function()

# Python will treat a as local variable due to assignment on line 5 in
# funciton definition will raise an error. printing before assignment. 