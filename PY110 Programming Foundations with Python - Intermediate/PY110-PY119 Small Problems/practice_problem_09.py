# input: 2 strings
# output: Integer
# rules
#   Explicit:
#       - Returns the number of times that the second string occurs
#         in the first string.
#       - The second argument will never be an empty string.
#       - Overlapping strings don't count.
# Test Cases and Examples
#   print(count_substrings('babab', 'bab') == 1)
#   print(count_substrings('babab', 'ba') == 2)
#   print(count_substrings('babab', 'b') == 3)
#   print(count_substrings('babab', 'x') == 0)
#   print(count_substrings('babab', 'x') == 0)
#   print(count_substrings('', 'x') == 0)
#   print(count_substrings('bbbaabbbbaab', 'baab') == 2)
#   print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
#   print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
# Data Structure and Algorithm
#   - Initialize substrings to all_substrings(string, substring) - HELPER FUNCTION
#   - Initialize substrings_count to 0
#   - Iterate over each substring in substrings
#       - Initialize count to:
#         count second argument in substring
#       - If count > substrings_count:
#           - Reassign substrings_count to count
#   - Return substrings_count

# HELPER FUNCTION : all_substrings(string, substring)
#   - Initialzie subsring_length = len(substring)
#   - Initialize idx = 0
#   - Initialize substrings to empty list.
#   - while idx <= (len(string) - substring_length)
#       - Intialize s_idx = idx
#       - Initialize e_idx = s_idx + substring_length
#       - Initialize sub_list to empty list
#       - while e_idx is less than equal to length of the string:
#           - current_substring = string[s_idx:e_idx]
#           - add current_substring to sub_list
#           - s_idx = e_dex
#           - e_idx = s_idx + substring_length
#       - Add sublist to substrings
#       - Add idx value by 1
#   - Return substrings     

# def all_substrings(string, substring):
    # substring_length = len(substring)
    # idx = 0
    # substrings = []
    # while idx < (len(string) - substring_length):
        # s_idx = idx
        # e_idx = s_idx + substring_length
        # sub_list = []
        # while e_idx <= len(string):
            # current_substring = string[s_idx:e_idx]
            # sub_list.append(current_substring)
            # s_idx = e_idx
            # e_idx = s_idx + substring_length
        # substrings.append(sub_list)
        # idx += 1
    
    # return substrings

# def count_substrings(string, substring):
    # substrings = all_substrings(string, substring)
    # substrings_count = 0
    # for substrings_lst in substrings:
        # count = substrings_lst.count(substring)
        # if count > substrings_count:
            # substrings_count = count
    
    # return substrings_count

def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

