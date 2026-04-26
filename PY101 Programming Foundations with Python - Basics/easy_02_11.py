# input: non-empty string
# output: Return string i.e. if string has an odd length, we should
#         return exactly one character string, if string has an even
#         length, we should return exactly two characters. If it is 
#         even, we should return char at half + 1 (for example if 
#         length is 12, we should return 6th (12 // 2) and 7th char). If 
#         it is odd we should return char exact at half. (for example
#         if length is 13, we should return 7th char (13 // 2))
# Test Cases:
#   print(center_of('I Love Python!!!') == "Py")    # True
#   print(center_of('Launch School') == " ")        # True
#   print(center_of('Launchschool') == "hs")        # True
#   print(center_of('Launch') == "un")              # True
#   print(center_of('Launch School is #1') == "h")  # True
#   print(center_of('x') == "x")                    # True
# Data Structure and Algorithm
#   a. initialize the length = length of the string
#   b. intialize middle_index = lenght of the string // 2
#   c. If length is odd:
#           return string[middle_index]
#      else:
#           return string[middle_index - 1:middle_index + 1]


def center_of(string):
    length = len(string)
    middle_index = length // 2
    if length % 2 == 1:
        return string[middle_index]
    else:
        return string[middle_index - 1:middle_index + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
print(center_of('xy') == "xy")                  # True