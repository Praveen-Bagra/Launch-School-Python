# def squared_greet(num, name):
    # squared_num = num * num
    # print(f"Hello {name}, your number squared is {squared_num}.")

# squared_greet(5, 'Srdjan')
# squared_greet('Srdjan', 5)

# animals = ['cat', 'mouse', 'dog', 'tiger', 'lion']
# print(sorted(animals, key=len))

# def greet(name, color=None):
    # if color:
        # print(f'Hello {name}. Your favorite color is {color}.')
    # else:
        # print(f"Hello {name}. You don't have a favorite color.")

# greet("Max", color='blue')
# greet("Max", 'blue')
# greet(color='blue', name='Max')
# greet(name='Max', color='blue')

def greet(name, color='blue'):
    print(f'Hello {name}. Your favorite color is {color}.')