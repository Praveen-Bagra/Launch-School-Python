numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = [ num // 2 for num in numbers.values() ]
print(half_numbers)

half_numbers = []
for num in numbers.values():
    half_numbers.append(num // 2)

print(half_numbers)