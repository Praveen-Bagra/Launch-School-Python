# 1. input = Whole number (It can be either positive or negative) 
#    output = Returns true if number's absolute value is odd, otherwise
#             False 
# 2. Test cases:
#       whether_odd(0) # Returns False
#       Whether_odd(1) # Returns True
#       whether_odd(-1) # Returns True
#       whether_odd(100) # Retruns False
#       whether_odd(-99) # Returns True
# 3 & 4. Data Structure and Algorithm:
#       a. First convert the argument number into absolute number 
#          and save it to abs_number.
#           i. If it is less than 0, mulitiple the number by -1 and 
#              assign it to abs_number, otherwise assign the same
#              number to abs_number.
#       b. Divide the abs_number by 2 and check if the remainder = 1
#          returns True, otherwise False

def abs_num(num):
    if num < 0:
        return num * -1
    else:
        return num

def whether_odd(number):
    if (abs_num(number) % 2) > 0:
        return True
    else:
        return False

     

print(whether_odd(0)) # Returns False 
print(whether_odd(1)) # Returns True
print(whether_odd(-1)) # Returns True
print(whether_odd(100)) # Retruns False
print(whether_odd(-99)) # Returns True