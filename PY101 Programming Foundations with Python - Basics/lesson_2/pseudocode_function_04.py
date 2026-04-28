# a function that determines the index of the 3rd occurrence of a given 
# character in a string. For instance, if the given character is 'x' 
# and the string is 'axbxcdxex', the function should return 6 (the 
# index of the 3rd 'x'). If the given character does not occur at least
# 3 times, return None

# START

# Given the string and the character

# SET counter = 0
# SET idx = 0
# WHILE idx < length of string # Iterate over 
#       IF character is equal to char
#           SET counter += 1
#       IF counter == 3
#           PRINT idx
#       idx += 1       
#
# PRINT None

def find_third_occurence_index(string, character):
    counter = 0
    idx = 0
    while idx < len(string):
        if string[idx] == character:
            counter += 1
        if counter == 3:
            return idx
        idx += 1

    return None

print(find_third_occurence_index('axbxcdxex','z'))