# input: number as year
# output: Returns century number with appropriate prefix i.e. 'st',
#         'nd', 'rd', or 'th'. New centuries begin in years that end 
#         in 01.
# Test Cases:
#   print(century(2000) == "20th")          # True
#   print(century(2001) == "21st")          # True
#   print(century(1965) == "20th")          # True
#   print(century(256) == "3rd")            # True
#   print(century(5) == "1st")              # True
#   print(century(10103) == "102nd")        # True
#   print(century(1052) == "11th")          # True
#   print(century(1127) == "12th")          # True
#   print(century(11201) == "113th")        # True
# Data Structure and Algorithm:
#   a. if number % 100 == 0, then return number // 100 else 
#       (number // 100) + 1
#   b Check last digit of century, if 1, add st, if 2 add nd, if 3
#     add rd else add th to the century number and return as string. 
#     If last two digtis are between 11 and 13 inclusive, than add
#     th to the century

def century(year):
    century_str = ''
    if year % 100 == 0:
        century_str = str(year // 100)
    else:
        century_str = str((year // 100) + 1)

    if 11 <= int(century_str[-2:]) <= 13: # Checks last 2 digit
        return century_str + 'th'
    else:
        match century_str[-1]: # Checks last digit
            case '1':
                return century_str + 'st'
            case '2':
                return century_str + 'nd'
            case '3':
                return century_str + 'rd'
            case _:
                return century_str + 'th'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True