# input: list containing numbers
# output: string
# rules
#   Explicit:
#       - Multiplies all of the integers together, divides the result
#         by the number of elements in the list
#       - Returns the result as a string with the value rounded to 
#         three decimal places.
#  Test Cases / Examples:
#   print(multiplicative_average([3, 5]) == "7.500")
#   print(multiplicative_average([2, 5, 8]) == "26.667")
#   print(multiplicative_average([2, 5]) == "5.000")
#   print(multiplicative_average([1, 1, 1, 1]) == "0.250")
#   print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
# Data Structure and Algorithm:
#   - Initialize variable multiplication_total to 1
#   - Iterate over each num:
#       multiplication total = multiplication total * num
#   - result = multiplication_total / length of the list
#   - return result formatted to 3 decimal places.

def multiplicative_average(lst):
    multiplication_total = 1
    for num in lst:
        multiplication_total *= num

    result = str(round((multiplication_total / len(lst)), 3))

    length_after_decimal = len(result.split('.')[1]) 

    if length_after_decimal == 1:
        return result + '00'
    if length_after_decimal == 2:
        return result + '0'
    
    return result


    # return f'{result:.3f}'



# All of these examples should print True
print(multiplicative_average([3, 5])  == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
print(multiplicative_average([25, 25, 25, 25, 25])  == "1953125.000")