# names = ('Chris', 'Pete', 'Nick')
# chris, pete, *remaining_names = names
# print(remaining_names)

# names = ('Chris', 'Pete', 'Nick', 'Brandi', 'Clare')
# chris, pete, *remaining_names = names
# print(remaining_names)

# numbers = [10, 50, 20, 30, 40, 60, 70]
# start = numbers[0:-1]
# last = numbers[-1]
# print(start)
# print(last)

# numbers = [10, 50, 20, 30, 40, 60, 70]
# *start, final = numbers
# print(start)
# print(final)

numbers = [10, 50, 20, 30, 40, 60, 70]
first, second, *middle, last = numbers
print(first)
print(second)
print(middle)
print(last)