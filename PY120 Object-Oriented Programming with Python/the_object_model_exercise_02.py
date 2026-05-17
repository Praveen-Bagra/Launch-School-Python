class Foo:
    
    def __init__(self, name):
        self.name = name

foo_object = Foo('Foo_name')

print(f'I am a {foo_object.__class__.__name__} object.')
print(f'I am a {type(foo_object).__name__} object.')

