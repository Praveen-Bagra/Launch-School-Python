number = 4936

one_place = number % 10
number = number // 10

tens_place = number % 10
number = number // 10

hundreds_place = number % 10
number = number // 10

thousands_place = number

print(f'One place is {one_place}')
print(f'Tens place is {tens_place}')
print(f'Hundreds place is {hundreds_place}')
print(f'Thousands place is {thousands_place}')