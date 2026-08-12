square = lambda number: number**2
hello = lambda: print('hello')
add3 = lambda num1, num2, num3: num1 + num2 + num3

print(square(2))
hello()
print(add3(1, 2, 3))

numbers = [1, 2, 3, 4, 5]
transformed = map(lambda number: number**2, numbers)
print(list(transformed))

strings = ['cat', 'dog', 'bird', 'fish']
transformed = map(lambda string: string.upper(), strings)
print(list(transformed))

numbers = [1, 2, 3, 4, 5]
selected = filter(lambda num: num % 2 == 0, numbers)
print(list(selected))