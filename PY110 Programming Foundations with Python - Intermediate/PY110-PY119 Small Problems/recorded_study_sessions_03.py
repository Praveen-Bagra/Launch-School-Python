# input: string
# output: new list 
# rules:
#   Explicit:
#       - To return a list containing all substrings starting from
#         1st character in original string.
# Data Structure and Algorithm:
#   - Intialize variable sub_strings to empty list.
#   - Iterate for the number of times as per the length of the string:
#     idx should start from 1 
#       - Add sub_string based on slicing[idx (ending_idx)] to 
#         the substrings
#   - Return sub_strings

# Data Strucute and Algorithm: Return all substrings ending with last
# character
#   - Initialize substrings_ending_last_charater to empty list.
#   - Initialize starting_idx to 0
#   - Initialize ending_idx to length of the original string
#   - while starting_idx is less than length of the string - 1
#       - add string[starting_idx, ending_idx]
#       - Increase ending_idx value by 1

def all_substrings_ending_with_same_last_character(string):
    substrings_ending_same_last_characters = []
    starting_idx = 0
    ending_idx = len(string)
    while starting_idx < len(string):
        substrings_ending_same_last_characters.append(string[starting_idx:ending_idx])
        starting_idx += 1
    return substrings_ending_same_last_characters


word = 'Sesquipedalianism'

def parts(string):
    sub_strings = []
    for idx in range(1, len(string) + 1):
        sub_strings.append(string[:idx])

    return sub_strings

print(parts(word))

def all_substrings(string):
    all_substrings = []
    for substring in all_substrings_ending_with_same_last_character(string):
        for sub_sub_string in parts(substring):
            all_substrings.append(sub_sub_string)

    return all_substrings
    
print(all_substrings('abcd'))

# - Initialize all_substrings to empty list.
# - Initialize starting_idx to 0.
# - loop while starting_idx is less than length of the string.
#       - Initialize ending_idx = starting_idx + 1
#       - loop while ending_idx is less equal to length of the string
#           - add string[starting_idx:ending_idx] to all_substrings
#           - Increase ending_idx value by 1
#       - Increase starting_idx value by 1
# - Return all_substrings

def all_substrings2(string):
    all_substrings = []
    starting_idx = 0
    while starting_idx < len(string):
        ending_idx = starting_idx + 1
        while ending_idx <= len(string):
            substring = string[starting_idx:ending_idx]
            all_substrings.append(substring)
            ending_idx += 1
        starting_idx += 1
    
    return all_substrings

print(all_substrings('abcd'))