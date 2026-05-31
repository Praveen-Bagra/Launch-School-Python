# input: list
# output: Integer
# rules:
#   Explicit:
#       - To return the minium integer value that can be appended to
#         the list so the sum of all the elements equals the closest
#         prime number that is graater than the current sum of the
#         numbers.
#       - The list will always contain at least 2 integers.
#       - All values in the list will be positive
#       - There may be multiple occurences of the various numbers
#         in the list.
# Test Cases / Examples
#   print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
#   print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
#   print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
#   print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

#   # Nearest prime to 163 is 167
#   print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
# Data Structure and Algorithm:
#   - Initialize total_sum to sum of the orignal list
#   - Initialize current_num to total_sum
#   - while True
#       - current_num += 1
#       - Initialize multiple to 2
#       - while multiple is less than current_num 
#           - if current_num remainder multiple == 0
#               break
#           - Increase multiple value by 1
#       - break
#   - Return current_num - total_sum

def nearest_prime_sum(lst):
    total_sum = sum(lst)
    current_num = total_sum + 1
    while True:
        prime_found = True
        multiple = 2
        while multiple < current_num:
            if current_num % multiple == 0:
                prime_found = False 
                break
            multiple += 1
        if prime_found == True:
            break
        current_num += 1
    
    return current_num - total_sum
    
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)