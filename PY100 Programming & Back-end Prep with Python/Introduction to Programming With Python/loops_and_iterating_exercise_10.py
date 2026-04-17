import random

highest = 10
# number = 0
# # print(number)

# while number != highest:
    # number = random.randrange(highest + 1)
    # print(number)

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

