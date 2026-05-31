# input: string (may contain word or words)
# output: string
# rules:
#   Explicit:
#       - Every other character, starting from the first (idx 0), 
#         should be capitalized
#       - And character followed should be lowercase of non-alphabetic
#         character.
#       - Non-alphabetic characters should not be changed, but should
#         be counted as characters for determining when to switch 
#         between upper and lower case. It means they should be
#         counted for index purposes.
#   Implicit:
#       - Empty string should return empty string.
# Test Cases / Examples:
#   string = 'I Love Launch School!'
#   result = "I LoVe lAuNcH ScHoOl!"
#   print(staggered_case(string) == result)  # True

#   string = 'ALL_CAPS'
#   result = "AlL_CaPs"
#   print(staggered_case(string) == result)  # True

#   string = 'ignore 77 the 4444 numbers'
#   result = "IgNoRe 77 ThE 4444 nUmBeRs"
#   print(staggered_case(string) == result)  # True

#   print(staggered_case('') == "")          # True
# Data Structure and Algorithm:
#   - Intialize modified_string to empty string
#   - Iterate over each char with idx in original string
#       - if idx is even
#           Add char converted to uppercase to modified_string
#       - else
#           add char converted to lowercase to modified_string
#   - Return modified_string

def staggered_case(string):
    modified_string = ''
    for idx, char in enumerate(string):
        if idx % 2 == 0:
            modified_string += char.upper()
        else:
            modified_string += char.casefold()

    return modified_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True