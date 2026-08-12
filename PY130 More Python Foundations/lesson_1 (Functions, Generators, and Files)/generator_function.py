def count_up_to(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1

counter = count_up_to(5)
for number in counter:
    print(number)