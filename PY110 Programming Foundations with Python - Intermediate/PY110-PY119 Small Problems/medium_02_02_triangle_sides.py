# input: 3 Integers
# outpu: string
# rules:
#   - To return one of the followoing four strings
#       - 'equilateral', 'isosceles', 'scalene', 'invalid'
#   - equilateral: all three sides have the same length.
#   - isosceles: two sides have the same length, while the third is
#                differernt.
#   - scalene: all three sides have different lengths
#   - invalid: Every side must have a length greater than 0
#              And the sum of the lengths of the two shortest
#              sides must be greater than the length of the longest
#              side.
# Test Cases / Examples
#   print(triangle(3, 3, 3) == "equilateral")  # True
#   print(triangle(3, 3, 1.5) == "isosceles")  # True
#   print(triangle(3, 4, 5) == "scalene")      # True
#   print(triangle(0, 3, 3) == "invalid")      # True
#   print(triangle(3, 1, 1) == "invalid")      # True
# Data Structure and Algorithm:
#   - Intialze sides to: [side1, side2, side3]
#   - Initialize copy_sides to: sides.copy()
#   - Remove longest side from copy_sides
#   - If any of the side in sides is 0 or sum of copy sides < longest_side:
#       - return 'invalid'
#   - else if all three sides are equal:
#       - return 'equilateral'
#   - else if two sides are equal and third is different
#       - return 'isosceles'
#   - else if three sides are different
#       - return 'scalene'

def triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides_copy = sides.copy()
    longest_side = max(sides_copy)
    sides_copy.remove(longest_side)

    any_zero = [side == 0 for side in sides]
    if any(any_zero) or sum(sides_copy) < longest_side:
        return 'invalid'
    elif len(set(sides)) == 1:
        return 'equilateral'
    elif len(set(sides)) == 2:
        return 'isosceles'
    else:
        return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

    