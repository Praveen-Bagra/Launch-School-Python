# input: List
# output: Integer
# rules:
#   Explicit:
#       - Return the integer that appears an odd number of times.
#       - There will always one such integer in the input list
# Test Cases / Examples
#   print(odd_fellow([4]) == 4)
#   print(odd_fellow([7, 99, 7, 51, 99]) == 51)
#   print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
#   print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
#   print(odd_fellow([0, 0, 0]) == 0)
# Data Structure and Algorithm:
#   - Initialize number_and_counts to empty dictionary
#   - Iterate over the numbers list:
#       - If number is in the keys of number_and_counts:
#           - Increase its associated value by 1
#       - otherwise
#           - Insert number as key and value as 1 in number_and_counts
#   - Iterated over each number, count in number_and_counts:
#       - If count is odd
#           - return number

def odd_fellow(numbers):
    numbers_and_counts = {}
    for num in numbers:
        if num in numbers_and_counts:
            numbers_and_counts[num] += 1
        else:
            numbers_and_counts[num] = 1

    for number, count in numbers_and_counts.items():
        if count % 2 == 1:
            return number

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)