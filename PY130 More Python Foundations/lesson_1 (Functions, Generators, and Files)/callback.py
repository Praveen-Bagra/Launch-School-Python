# Callback Function
def foo(callback, my_list):
    for element in my_list:
        callback(element)

# Noncallback function
def foo(func, my_list):
    return {
        'func': func,
        'list': my_list.copy(),
    }