def count():
    count = 1
    while True:
        yield count
        count += 1

counter = count()
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3