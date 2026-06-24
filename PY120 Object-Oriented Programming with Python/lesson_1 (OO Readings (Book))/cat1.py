class Cat:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        return self.name

cat = Cat('Fuzzy')

print(cat)
print(f'My cat is {cat}')
print(cat.display())