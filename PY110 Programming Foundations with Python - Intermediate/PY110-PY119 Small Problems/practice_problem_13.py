# input: 2 strings
# output: Boolean i.e. True or False
# rules:
#   Explicit:
#       - To return True if some portion of the characters
#         in the first string can be rearranged to match
#         the characters in the second. Otherwise False
#       - Both strings contain lowercase alphabetic
#         characters. 
#       - Neither string will be empty.
# Test Cases / Examples
#   print(unscramble('ansucchlohlo', 'launchschool') == True)
#   print(unscramble('phyarunstole', 'pythonrules') == True)
#   print(unscramble('phyarunstola', 'pythonrules') == False)
#   print(unscramble('boldface', 'coal') == True)
#   print(unscramble('olc', 'cool') == False)
# Data Structure and Algorithm:
#   - Initialize variable char_counts to empty dictionary.
#   - Iterate over char in string2:
#       - If char is in char_counts
#           - Increase its associated value by 1
#       - Otherwise
#           - Insert char as key and value as 1 in char_counts
#   - Iterate over char, count in char_counts
#       - count_string1 = count char in string1
#       - If count_string1 < count
#           - return False
#   - Return True

def unscramble(string1, string2):
    char_counts = {}
    for char in string2:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char, count in char_counts.items():
        count_string1 = string1.count(char)
        if count_string1 < count:
            return False
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)