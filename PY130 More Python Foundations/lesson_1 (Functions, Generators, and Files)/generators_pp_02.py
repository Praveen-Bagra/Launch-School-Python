# def reciprocals(num):
    # for num in range(1, num + 1):
        # yield 1 / num

# for reciprocal in reciprocals(5):
    # print(reciprocal)

def reciprocals(num):
    number = 1
    while number <= num:
        yield 1 / number
        number += 1

for reciprocal in reciprocals(5):
    print(reciprocal)
