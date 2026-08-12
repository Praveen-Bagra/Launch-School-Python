def my_decorator(func):
    def wrapper():
        print('Before the function call')
        func()
        print("After the function call")

    return wrapper


@my_decorator
def say_hello():
    print('Hello!')

# decorated_hello = my_decorator(say_hello)
# decorated_hello()

say_hello()