# input: string
# output: string
# rules:
#   Explicit:
#       - Returns a string with every consonant doubled.
#       - Consonant are case insensitive. 'B' and 'b' both are consonants.
#   Implicit:
#       - Empty string should return empty string.
# Test Cases / Examples:
#   print(double_consonants('String') == "SSttrrinngg")
#   print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
#   print(double_consonants('July 4th') == "JJullyy 4tthh")
#   print(double_consonants('') == "")
# Data Structure and Algorithm:
#   - Initialize variable consonants to 'bcdf...z'
#   - initialize doubled_consonants_string to empty string.
#   - Iterate over each character in the orignal string.
#       - Check char(converted to lowercase), if it is in consonants:
#           - add character 2 times in doubled_consonants_string
#       - Otherwise
#           - add the same character to doubled_consonants_string
#   - Return doubled_consonants_string

def double_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    doubled_consonants_string = ''
    for char in string:
        if char.lower() in consonants:
            doubled_consonants_string += char * 2
        else:
            doubled_consonants_string += char

    return doubled_consonants_string

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")