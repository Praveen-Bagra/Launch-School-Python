# input: current age and retire age in string
# output: strings contaning current year and retire year and years to
#         work.
# Test Cases:
#   What is your age? 30
#   At what age would you like to retire? 70
#   It's 2024. You will retire in 2064.
#   You have only 40 years of work to go!
# Data Structure and Algorithm:
#   a. intialize total_years_to_work = retirement_age - current_age
#   b. initialize current_year and retirement year
#   c. print required starement contating current year and retirement 
#      year (current year + total_years_to_work)
#   d. Print required statement containing total_years_to_work.

from datetime import datetime

current_age = int(input('What is your age? '))
retirement_age = int(input('At what age would like to retire? '))

total_years_to_work = retirement_age - current_age
current_year = datetime.now().year
retirement_year = current_year + total_years_to_work

print()
print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {total_years_to_work} years of work to go!")


