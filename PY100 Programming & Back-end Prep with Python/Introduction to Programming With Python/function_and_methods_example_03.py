s = 'Hello World!'
t = 'Hello World!'
print(id(s))
print(id(t))
print(id(s) == id(t))

s = 'supercalifragilisticexpialidocious'
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))

x = 5
y = 5
print(id(x) == id(y))

x = 5
y = 6
print(id(x) == id(y))

a = "Hello, How are you? 123"
b = "Hello, How are you? 123"
print(id(a))
print(id(b))

e = [1, 2, 3]
f = [1, 2, 3]
print(id(e))
print(id(f))
print(id(e) == id(f))