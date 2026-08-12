data = (100, 200, 300, 400)
first, *_, last = data

print(first)
print(_)
print(last)

data = {'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400}
first, *_, last = data

print(first)
print(_)
print(last)