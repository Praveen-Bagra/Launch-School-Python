# def greet(name, /, *, color=None):
    # if color:
        # print(f"Hello {name}. Your favorite color is {color}.")
    # else:
        # print(f"Hello {name}. You don't have a favorite color.")

# greet("Pete")
# greet("Max", color='blue')
# greet("Max", 'blue')

def greet(*, name='John Doe', color=None):
    if color:
        print(f"Hello {name}. Your favorite color is {color}.")
    else:
        print(f"Hello {name}. You don't have a favorite color.")

greet()
greet(color='blue', name='Max')
greet('Max', color='blue')