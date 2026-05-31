# input: string
# output: string
# rules:
#   Explicit:
#       - Return a string with every character doubled.
#   Implicit:
#       - Empty string should return empty string.
# Test Cases / Examples:
#   print(repeater('Hello') == "HHeelllloo")              # True
#   print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
#   print(repeater('') == "")                             # True
# Data Structure and Algorithm:
#   - Initialize doubled_string to empty string.
#   - Iterate over each character in original string
#       Iterate for 2 times:
#           add char to doubled_string
#   - Return doubled_string

def repeater(string):
    # doubled_string = ''
    # for char in string:
        # for _ in range(2):
            # doubled_string += char
    
    # return doubled_string
    return ''.join([char for char in string for _ in range(2)])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True