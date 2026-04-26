# input: To print all even numbers from 1 to 99, inclusive.
# output: To print all even numbers on a seperate line.
# Test Cases:
#   2
#   4
#   ...
#   98
# Data Structure and Algorithm:
#   To iterate over the range from 1 to 99 inclusive.
#   Check if the number is even (num % 2 == 0), if it is then print it

# for num in range(1, 100):
    # if num % 2 == 0:
        # print(num)

for num in range(2, 100, 2):
    print(num)