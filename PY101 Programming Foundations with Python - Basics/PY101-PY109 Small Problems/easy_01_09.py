# input: number(year) greater than 0 i.e of 4 digits
# output: From 1752:
#          Boolean True or False. True if it is a leap year, otherwise
#          False.
#          Divisible by 4 but not divisible by 100, is a leap year
#          Not Divisible by 100 but divisible by 400, is a leap year
#         Before 1752:
#           Every 4 years is a leap year. Divisible by 4 
# Test Cases:
#   print(is_leap_year(1) == False)
#   print(is_leap_year(2) == False)
#   print(is_leap_year(3) == False)
#   print(is_leap_year(4) == True)
#   print(is_leap_year(1000) == True)
#   print(is_leap_year(1100) == True)
#   print(is_leap_year(1200) == True)
#   print(is_leap_year(1300) == True)
#   print(is_leap_year(1751) == False)
#   print(is_leap_year(1752) == True)
#   print(is_leap_year(1753) == False)
#   print(is_leap_year(1800) == False)
#   print(is_leap_year(1900) == False)
#   print(is_leap_year(2000) == True)
#   print(is_leap_year(2023) == False)
#   print(is_leap_year(2024) == True)
#   print(is_leap_year(2025) == False)
# Data Structure and Algorithm:
#   a. initialize result = False
#   b. Check: 
#       If year greater than equal to 1752
#           If divisible by 4, set result = True
#           If divisible by 100, set result = False
#           If divisible by 400, set result = True 
#       else
#           If divisible by 4, set result = True    
# Return the result

def is_leap_year(year):
    result = False
    if year >= 1752: 
        if year % 4 == 0:
            result = True
        if year % 100 == 0:
            result = False
        if year % 400 == 0:
            result = True
    else:
        if year % 4 == 0:
            result = True
    
    return result

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)