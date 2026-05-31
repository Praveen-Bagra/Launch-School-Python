# input: string
# output: integer
# rules:
#   # Explicit:
#       - Return the appropriate integer as per the string.
#       - The input string can contain signs, so we should return
#         the appropriate sign accordingly
#         For example '4321' should return 4321
#                      '-570' should return -570
#                      '+100' should return 100
#       - Shouldn't use any standard conversion functions
#         available in Python, such as 'int'.
#       - The string will always contain a valid number.
#       - Can use previous exercise function in solution
# Test Cases / Examples:
#   print(string_to_signed_integer("4321") == 4321)  # True
#   print(string_to_signed_integer("-570") == -570)  # True
#   print(string_to_signed_integer("+100") == 100)   # True
# Data Structure and Algorithm:
#   - if first character in string is '+' or '-':
#       initialize num_string = stirng 2nd character to last character
#   - else
#       initialize num_string = string
#   - If first_character in string is '-':
#       return string_to_integer(num_string) * -1
#   - Return string_to_integer(num_string)


def string_to_integer(string):
    numbers_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                    '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    num = 0
    multiplier = 1
    for num_str in string[::-1]:
        num += numbers_dict[num_str] * multiplier
        multiplier *= 10

    return num

def string_to_signed_integer(string):
    if string[0] in ['+', '-']:
        num_string = string[1:]
    else:
        num_string = string

    if string.startswith('-'):
        return string_to_integer(num_string) * -1

    return string_to_integer(num_string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
