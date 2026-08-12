foo0 = 1
print(hex(id(foo0)))

def bar1():
    foo1 = 2
    print(hex(id(foo1)))

    def bar2():
        foo2 = 3
        print(foo0)
        print(foo1)
        print(foo2)

    def bar3():
        foo3 = 3
        print(foo)
        print(foo1)
        print(foo3)

    return bar2, bar3

func2, func3 = bar1()
print(bar1.__closure__)
print(func2.__closure__)
print(func3.__closure__)
print(func2.__closure__ is func3.__closure__)
print()



def create_greeting():
    greeting = 'Hello'
    print(hex(id(greeting)))

    def display_greeting():
        print(greeting)

    return display_greeting

greet = create_greeting()
greet()
print(greet.__closure__)
