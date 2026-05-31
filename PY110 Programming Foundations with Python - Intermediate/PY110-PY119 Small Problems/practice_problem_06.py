# input: string
# output: a new dict
# rules
#   Explicit:
#       - To return a dictionary containg lowercase letters as keys
#          and their counts in the string.
#       - If the characters are uppercase 
#   Implicit:
#       - If the string is empty, return empty dictionary
# Test Cases / Examples
#   expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
#   print(count_letters('woebegone') == expected)

#   expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            #   'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
#   print(count_letters('lowercase/uppercase') == expected)

#   expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
#   print(count_letters('W. E. B. Du Bois') == expected)

#   print(count_letters('x') == {'x': 1})
#   print(count_letters('') == {})
#   print(count_letters('!!!') == {})
# Data Structure and Algorithm:
#   - Intialize alphabets = 'abc...z'
#   - Intialize letters_and_counts to empty dictionary.
#   - Iterate for each char in string:
#       - If is in alphabets and in letters_and_counts:
#           - Increase associated char value by 1
#       - Elif it is in alphabets
#           - Add char key and value as 1 in letters_and_counts
#   - Return letters_and_counts

def count_letters(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    letters_and_counts = {}
    for char in string:
        if (char in alphabets) and (char in letters_and_counts):
            letters_and_counts[char] += 1
        elif char in alphabets:
            letters_and_counts[char] = 1
    
    return letters_and_counts

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
            
