# input: string & number
# output: prints string at number of times
# Test Cases:
#   repeat('Hello', 3)
#   # Prints
#       Hello
#       Hello
#       Hello
# Data Structure and Algorithm:
#   a. Iterate over the range(number):
#       print string

def repeat(string, number_of_times):
    for _ in range(number_of_times):
        print(string)

repeat('Hello', 3)