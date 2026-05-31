# input = string
# output = string (a single character)
# rules:
#   Explicit:
#       - Returns the character that occurs most often in the string.
#       - If there are multiple characters with the same greatest
#         frequency, return the one that appears first in the string.
#       - When counting characters, consider uppercase and lowercase
#         versions to be the same.
#   Implicit:
#       - Return lower case version of character
# Test Cases / Examples
#   print(most_common_char('Hello World') == 'l')
#   print(most_common_char('Mississippi') == 'i')
#   print(most_common_char('Happy birthday!') == 'h')
#   print(most_common_char('aaaaaAAAA') == 'a')

#   my_str = 'Peter Piper picked a peck of pickled peppers.'
#   print(most_common_char(my_str) == 'p')

#   my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
#   print(most_common_char(my_str) == 'e')
# Data Structure and Algorithm
#   - convert string to lowercase
#   - Initialize counts to empty dictionary
#   - Iterate over each character in string:
#       - If char is in counts keys:
#           - Increase its associated value by 1
#       - else
#           - Add that char as key and value as 1 to counts
#   - Convert count keys as list
#   - Sort it based on dictionary assoicated value. Highest should be first.
#   - Return counts first element that is character.

def most_common_char(string):
    string = string.casefold()
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    def count_key(char):
        return counts[char]

    characters = list(counts.keys())
    characters.sort(key=count_key, reverse=True)
    return characters[0]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')