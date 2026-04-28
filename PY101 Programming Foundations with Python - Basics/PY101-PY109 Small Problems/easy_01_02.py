# 1. input: To print all the oldd numbers from 1 to 99, inclusive.
#    output: To print each number on seperate line.
# 2. Test Cases:
#       1
#       3
#       ...
#       99
# 3. Data Structure and Algorithm:
#      a. To iterate over the range from 1 to 99 
#      b. Check the number. If is is odd (num % 2 == 1), then print
#       each number.

for num in range(1, 100):
    if (num % 2) == 1:
        print(num)


# for num in range(1, 100, 2):
    # print(num)