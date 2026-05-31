# input: string
# output: Boolean True or False
# rules:
#   Explicit:
#       - Return True if all parenthesis in the string are properly
#         balanced, False otherwise.
#       - Properly balanced parenthesis means, parentheses must
#         occur in matching '(' and ')' pairs.
#   Implicit
#       - String may not contain any parenthesis at all. It should
#         return True.
# Examples / Test Cases:
#   print(is_balanced("What (is) this?") == True)        # True
#   print(is_balanced("What is) this?") == False)        # True
#   print(is_balanced("What (is this?") == False)        # True
#   print(is_balanced("((What) (is this))?") == True)    # True
#   print(is_balanced("((What)) (is this))?") == False)  # True
#   print(is_balanced("Hey!") == True)                   # True
#   print(is_balanced(")Hey!(") == False)                # True
#   print(is_balanced("What ((is))) up(") == False)      # True
# Data Structure and Algorithm:
#   - Set variable check to 0.
#   - Iterate over each character in the original string
#       - If character is '('
#           - Increase check by 1
#       - Else if character is ')'
#           - Decrease check by 1
#       - If check value is less than 0
#           - Return False
#   - If check value is greater than 0
#       - Return False
#   - Return True

def is_balanced(string):
    check = 0
    for char in string:
        if char == '(':
            check += 1
        elif char == ')':
            check -= 1

        if check < 0:
            return False
    
    if check > 0:
        return False
    
    return True

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True