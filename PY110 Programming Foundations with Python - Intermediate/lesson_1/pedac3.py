# input: integer (the row number)
# output: integer (the sum of numbers in that row)
# rules:
#   Explicit:
#       1. The row starts with even integer 2.
#       2. The first row contain one integer, the second row contains 
#          two integers and so on... 
#       3. It's a sequence of even integer
#       4. It looks like row-wise:
#           2
#           4, 6
#           8, 10, 12
#           14, 16, 18, 20
# Test Cases:
#   Row number: 1 -> Sum of integers in row: 2
#   Row number: 2 -> Sum of integers in row: 10
#   Row number: 4 -> Sum of integers in row: 68
# Data Structure / Algorithm:
#   - Declare result variable and initialize to empty list.
#   - Declare start variable and initialize it to 2 integer.
#   - Iterate for the number of times as per input number:
#       - declare stop variable and initialize to start + (2 * times iterated)
#       - append start to stop inclusive integers incremented by 2 as list.
#       - start = result last object's last element + 2
#   - return result list last element's sum of integers.

def sum_of_even_integers_in_a_row(num):
    result = []
    start = 2
    for iteration in range(num):
        stop = start + (2 * iteration)
        result.append(list(range(start, (stop + 1), 2)))
        start = result[-1][-1] + 2

    return sum(result[-1])

print(sum_of_even_integers_in_a_row(1))
print(sum_of_even_integers_in_a_row(2))
print(sum_of_even_integers_in_a_row(4))


