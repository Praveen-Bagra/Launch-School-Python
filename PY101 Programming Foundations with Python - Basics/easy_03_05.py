# input: positive integer
# output: prints string i.e. stars in triangle format whose sides have
#         positive integer stars. The diagonal should have one end at
#         lower left and one at upper right
# Test Cases:
#   triangle(5)
    # *
   # **
  # ***
 # ****
# *****
# triangle(9)
        # *
       # **
      # ***
     # ****
    # *****
   # ******
  # *******
 # ********
# *********
# Data Structure and Algorithm:
#   a. initialize space_counter = side - 1
#   b. initialize star_counter = 1
#   c. Iterater over the range(side)
#           print ' ' * space_counter + '*' * star_counter
#           space_counter -= 1
#           star_counter += 1


def triangle(side):
    space_counter = side - 1
    star_counter = 1
    for _ in range(side):
        print((' ' * space_counter) + ('*' * star_counter))
        space_counter -= 1
        star_counter += 1 

triangle(5)
print()
triangle(9)
