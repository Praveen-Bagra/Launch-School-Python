# input = string i.e name
# output = Print string i.e. greeting (Hello name.), If there is ! in 
#          the name in the last than (HELLO NAME! WHY ARE WE YELLING?) 
# Test Cases:
#   What is your name? Sue # Prints Hello Sue.
#   What is your name? Bob! # HELLO BOB! WHY ARE WE YELLING?
# Data Structure and Algorithm:
#   a. Check if there is ! in the last in the name. If it is:
#           print yelling greeting
#       else
#           print normal greeting


name = input('What is your name? ')
if name[-1] == '!':
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name.title()}.')
