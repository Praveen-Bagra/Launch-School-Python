def number_generator():
    for num in range(1, 6):
        yield num

for num in number_generator():
    print(num)