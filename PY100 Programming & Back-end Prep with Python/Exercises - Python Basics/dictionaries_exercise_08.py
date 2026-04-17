car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

result = []
for key, value in list(car.items()):
    result.append([key, value])

print(result)