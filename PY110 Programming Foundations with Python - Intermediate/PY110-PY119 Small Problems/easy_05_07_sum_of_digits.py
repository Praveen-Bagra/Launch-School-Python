def sum_digits(num):
    # sum_of_digits = 0
    # for num_str in str(num):
        # sum_of_digits += int(num_str)

    # return sum_of_digits
    numbers = [int(num_str) for num_str in str(num)]
    return sum(numbers)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True