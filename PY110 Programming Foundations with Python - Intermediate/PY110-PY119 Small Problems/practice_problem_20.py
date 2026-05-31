# input: list
# output: integer
# rules:
#   explicit:
#       - Return the number in the list that differs from all the rest.
#       - The list will contain at least 3 numbers, and there will be
#         exactly one number that is different.
# Test Cases / Examples:
#   print(what_is_different([0, 1, 0]) == 1)
#   print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
#   print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
#   print(what_is_different([3, 4, 4, 4]) == 3)
#   print(what_is_different([4, 4, 4, 3]) == 3)
# Data Structure and Algorithm:

def what_is_different(numbers):
    number_and_counts = {}
    for number in numbers:
        if number in number_and_counts:
            number_and_counts[number] += 1
        else:
            number_and_counts[number] = 1

    for number, count in number_and_counts.items():
        if count == 1:
            return number

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)