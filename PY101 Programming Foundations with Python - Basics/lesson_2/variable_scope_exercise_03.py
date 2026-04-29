num = 5

def my_func():
    global num
    num = 10

my_func()
print(num) # It will print 10. Since we have invoked the function
           # my_func() on line 7. And inside the function, we have
           # global num code, it means we can reassign the global 
           # variable num. On line 5 in insdie the function, we are 
           # reassigning num to 10. So now global variable num refrences
           # a new object 10. Hence it prints 10 when we call a function
           # print by passing its value as an argument.