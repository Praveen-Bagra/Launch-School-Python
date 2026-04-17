age = int(input("How old are you? "))
print()
print(f'You are {age} years old.')
for future in range(10, 45, 10):
    print(f'In {future} years, you will be ' 
          f'{age + future} years old.')
