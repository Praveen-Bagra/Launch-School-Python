# input: string (may contain word or words)
# output: string
# rules:
#   Explicit:
#       - Every other character, starting from the first (idx 0), 
#         should be capitalized
#       - And character followed should be lowercase of non-alphabetic
#         character.
#       - Non-alphabetic characters should not be changed, but should
#         not be counted as characters for determining when to switch 
#         between upper and lower case. It means they should be
#         ignored for index purposes.
#   Implicit:
#       - Empty string should return empty string.
# Test Cases / Examples:
#   string = 'I Love Launch School!'
#   result = "I lOvE lAuNcH sChOoL!"
#   print(staggered_case(string) == result)  # True

#   string = 'ALL_CAPS'
#   result = "AlL_cApS"
#   print(staggered_case(string) == result)  # True

#   string = 'ignore 77 the 4444 numbers'
#   result = "IgNoRe 77 ThE 4444 nUmBeRs"
#   print(staggered_case(string) == result)  # True

#   print(staggered_case('') == "")          # True
# Data Structure and Algorithm:
#   - Initialize variable modified_string to empty string.
#   - Intialize idx = 0
#   - Iterate over character in string:
#       - If character is alphabet
#           - If idx is even:
#               - add char (converted to upper case) to modified_string
#           - Else
#               - add char (converted to lower case) to modified_string
#           - Increase idx value by 1
#       - else
#           - add char (as it is) to modified_string
#   - Return modified_string

def staggered_case(string):
    modified_string = ''
    idx = 0
    for char in string:
        if char.isalpha():
            if idx % 2 == 0:
                modified_string += char.upper()
            else:
                modified_string += char.casefold()

            idx += 1
        else:
            modified_string += char
    
    return modified_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

            
            