bar = 42
qux = [1, 2, 3]
baz = 3

def foo(lst):
    value = lst.pop()
    print(f'popped {value} from the list')
    return value + bar + baz

foo(qux)

# It mutates the value of the object referenced by non-local variable
# i.e. qux
# It prints to the console.