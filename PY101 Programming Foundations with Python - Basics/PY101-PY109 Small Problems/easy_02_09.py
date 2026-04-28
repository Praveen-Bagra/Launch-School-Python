# input: Instruction to generate a random number between 20 and
#        100, inclusive as Teddy's age
# output: string. To print a sentence containing Teddy's age.
# Test Cases:
#   Teddy is 69 years old!
# Data Structure and Algorithm:
#   a. intialize age = random number between 20 and 100, inclusive.
#   b. Print Teddy's age statement containing age.

import random

age = random.randint(20, 100)
print(f'Teddy is {age} years old!')