# input: Integer
# output: Integer
# rules:
#   - Return the maximum number we can obtain by deleting exactly one
#     digit of the given number.
# Test Cases / Examples
#   - print(delete_digits(791983) == 91983)
#   - print(delete_digits(152) == 52)
#   - print(delete_digits(1001) == 101)
#   - print(delete_digits(10) == 1)
# Data Structure and Algorithm:
#   - convert num to string
#   - Initialize numbers to empty list.
#   - Intialize times to length of the num converted to string - 1
#   - Initialize starting_idx to 1
#   - Iterate for the number of times
#       - set ending_idx = starting_idx + 1
#       - num_str = string[:staring_idx] + string[ending_idx:]
#       - num_int = int(num_str)
#       - Add num_int to numbers 
#       - Increaes starting_idx value by 1  
#   - Add string second element to last element converted into integer
#     to numbers
#   - Return max number from numbers.

def delete_digits(num):
    num_str = str(num)
    numbers = []
    times = len(num_str) - 1
    starting_idx = 1
    for _ in range(times):
        ending_idx = starting_idx + 1
        number_str = num_str[:starting_idx] + num_str[ending_idx:]
        number_int = int(number_str)
        numbers.append(number_int)
        starting_idx += 1

    numbers.append(int(num_str[1:])) 
    
    return max(numbers)

print(delete_digits(791983) == 91983)
print(delete_digits(152) == 52)
print(delete_digits(1001) == 101)
print(delete_digits(10) == 1)