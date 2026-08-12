def greet_all(*names):
    for name in names:
        print(f"Hello, {name}.")

# staff = ['Chris', 'Pete', 'Nick']
staff = ('Chris', 'Pete', 'Nick')
# greet_all(staff[0], staff[1], staff[2])
greet_all(*staff)



