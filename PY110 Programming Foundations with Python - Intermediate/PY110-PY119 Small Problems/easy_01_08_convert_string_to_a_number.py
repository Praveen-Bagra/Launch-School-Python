# input: string
# output: integer
# rules:
#   # Explicit:
#       - Return the appropriate integer as per the string.
#         For example '4321' should return 4321
#                      '570' should return 570
#       - Shouldn't use any standard conversion functions
#         available in Python, such as 'int'.
#       - Should be calculated by using the characters in the string.
#       - All characters in the string will be numeric. There will be
#         no + or - signs in the string.
# Test Cases / Examples:
#   print(string_to_integer("4321") == 4321)  # True
#   print(string_to_integer("570") == 570)    # True
# Data Structure and Algorithm:
#   - Initialize variable numbers_dict to:
#     dictionary as {'1': 1, '2': 2, ... upto '0': 0}
#   - Initialize num to 0
#   - Initialize multiplier to 1
#   - Iterate over each num_str in reversed string:
#       - num += assoicate num_str value in numbers_dict * multiplier
#       - mulitiper *= 10
#   - Return num

def string_to_integer(string):
    numbers_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                    '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    num = 0
    multiplier = 1
    for num_str in string[::-1]:
        num += numbers_dict[num_str] * multiplier
        multiplier *= 10

    return num

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

