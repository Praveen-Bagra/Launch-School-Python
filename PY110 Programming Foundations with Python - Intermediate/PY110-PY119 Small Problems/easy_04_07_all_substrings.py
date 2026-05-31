# input: string
# output: list of all substrings
# rules:
#   Explicit:
#       - Returns a list of all substrings of a string.
#       - All substrings that start at index position 0 should
#         come first.
#       - Then all substrins that start at index position 1 and so on...
#       - Return the substrings at a given index from shortest to
#         longest.
#   Implicit:
#       - Assumed empty string should return empty list.
# Examples / Test Cases:
#   expected_result = [
    #   "a", "ab", "abc", "abcd", "abcde",
    #   "b", "bc", "bcd", "bcde",
    #   "c", "cd", "cde",
    #   "d", "de",
    #   "e",
#   ]
#   print(substrings('abcde') == expected_result)  # True
# Data Structure and Algorithm:
#   - Initialize variable substrings = []
#   - Initiazlize variable start_idx = 0
#   - while start_idx is less length of the string
#       - Initialize end_idx = start_idx + 1
#       - while end_idx is less than equal to length of the string
#           - Add string[start_idx:end_idx] to substrings
#           - Increase end_idx value by 1
#       - Increase start_idx value by 1
#   - Return substrings

def substrings(string):
    sub_strings = []
    start_idx = 0
    while start_idx < len(string):
        end_idx = start_idx + 1
        while end_idx <= len(string):
            sub_strings.append(string[start_idx:end_idx])
            end_idx += 1
        start_idx += 1
    
    return sub_strings

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True