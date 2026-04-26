# input: Bill amount and percentage amount.
# output: print tip amount and total amount
# Test Cases:
#   1. Bill is 200, tip percentage is 20 # Should print tip as 40
#                                          and total as 240
# Data Structure and Algorithm:
#   a. Ask the user for bill amount and tip percentage. Convert themn 
#      into floats.  
#   b. Initilize tip amount. Calculate the tip amount i.e. 
#      bill amount * (percent/10). 
#   c. Intialize and calculate total amount. Total amount = bill
#      amount + tip. 
#   d. Print tip amount and total amount. Round them off to 2 digits.

bill_amount = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? ')) 
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount

print()
print(f'The tip is ${tip_amount:.2f}')
print(f'The total is ${total_amount:.2f}')