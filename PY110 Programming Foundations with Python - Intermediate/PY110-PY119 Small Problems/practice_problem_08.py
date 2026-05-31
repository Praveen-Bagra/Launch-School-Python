# input: String
# output: Integer
# rules:
#   Explicit:
#       - The input string will be non-empty.
#       - The string will always contain lowercase alphabetic characters.
#       - The function should return the length of the longest vowel
#         substring. The vowels are a, e, i, o, u.
# Test Cases and Examples:
#   print(longest_vowel_substring('cwm') == 0)
#   print(longest_vowel_substring('many') == 1)
#   print(longest_vowel_substring('launchschoolstudents') == 2)
#   print(longest_vowel_substring('eau') == 3)
#   print(longest_vowel_substring('beauteous') == 3)
#   print(longest_vowel_substring('sequoia') == 4)
#   print(longest_vowel_substring('miaoued') == 5)
# Data Structure and Algorithm:
#   - Initialize substrings to all_substrings(string) - HELPER function
#   - Initialize vowels to 'aeiou'
#   - Initialize consecutive_vowels_count to 0
#   - Iterate over each substring in substrings
#       - Initialize vowels_count = 0
#       - Intialize all_vowels = True
#       - Iterate over each char in substring
#           - if char is non in vowels:
#               - Reassign all_vowels = False
#           - elif char in vowels:
#               - increase vowels_count by 1
#           - if vowels_count > consecutive_vowels_count and all_vowels == True
#               - Reassign consecutive_vowels_count to vowels_count
#   - Return consecutive_vowels_count
#            
#  HELPER Function (all_substrings)
#       - Intialize s_idx to 0
#       - Initialize substrings to empty list
#       - while s_idx < length of the string
#           - e_idx = s_idx + 1
#           - while e_idx <= length of the string
#               - Add string[s_idx:e_idx] to substrings
#               - Increase e_idx value by 1
#           - Increase s_idx value by 1
#       - Return substrings

def all_substrings(string):
    s_idx = 0
    substrings = []
    while s_idx < len(string):
        e_idx = s_idx + 1
        while e_idx <= len(string):
            substrings.append(string[s_idx:e_idx])
            e_idx += 1
        s_idx += 1
    
    return substrings

def longest_vowel_substring(string):
    substrings = all_substrings(string)
    vowels = 'aeiou'
    consecutive_vowels_count = 0
    for substring in substrings:
        vowels_count = 0
        all_vowels = True
        for char in substring:
            if char not in vowels:
                all_vowels = False
            elif char in vowels:
                vowels_count += 1
        
        if (vowels_count > consecutive_vowels_count) and (all_vowels == True):
            consecutive_vowels_count = vowels_count

    return consecutive_vowels_count

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
