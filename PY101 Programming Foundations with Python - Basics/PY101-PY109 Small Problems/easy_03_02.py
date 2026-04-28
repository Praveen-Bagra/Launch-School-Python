# input: string. Maybe with consecutive duplicate characters.
# output: Returns new string that contains original string value with
#         consecutive duplicates collapsed into single character.
#
# Test Cases:
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')
#
# Data Structure and Algorithm:
#   a. intialize result = [] 
#   b. if length of the string is greater than 0:
#       result.append(string[0])
#       remaining_char = string[1::]
#   c. Iterate over the remaining characters string
#       If char is not equal to last result elment
#           then append the character
#   d. Return string by joining result

def crunch(string):
    result = []
    if len(string) > 0:
        result.append(string[0])
        remaining_char_string = string[1::]
        for char in remaining_char_string:
            if char != result[-1]:
                result.append(char)
    
    return ''.join(result)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')