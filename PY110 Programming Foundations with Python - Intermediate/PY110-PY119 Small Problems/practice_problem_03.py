# input: string
# output: new string
# rules
#   Explicit:
#       - Return the copy of the string with every second character in every
#         third word converted to uppercase.
#       - Other character should reamin the same.
#   Implicit:
#       - Words are stirngs seperated by single whitespace.
#       - If third, sixth and so on...doesn't have second character, 
#         retunr the word as it is.
# Test Cases / Examples:
#   original = 'Lorem Ipsum is simply dummy text of the printing world'
#   expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
#   print(to_weird_case(original) == expected)

#   original = 'It is a long established fact that a reader will be distracted'
#   expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
#   print(to_weird_case(original) == expected)

#   print(to_weird_case('aaA bB c') == 'aaA bB c')

#   original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
#   expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
#   print(to_weird_case(original) == expected)
# Data Structure and Algorithm:
#   - Initialize variable 'words' to:
#     split the stirng by single whitespaice and save these words in a list.
#   - Initialize idx to 1
#   - Initialize 'modified_words' to empty list.
#   - Iterate over each word in words:
#       - If idx is multiple of 3 and length of word is more than equal to 2
#           - word = word with 2nd character capitalized
#       - add word to modified_words
#       - Increase idx value by 1.
#   - Returend modified words joined with single whitespace as string.

# Helper function: capitalize_second_character
# Intialize idx to 1
# Intialize 'modified_word' to empty string.
# I will iterate over the character in word
#   - If idx is multiple of 2
#       char = capitalize char
#   - add char to modified_word
# Return modified_word joined as string

def capitalize_second_character(word):
    idx = 1
    modified_word = ''
    for char in word:
        if idx % 2 == 0:
            char = char.upper()
        modified_word += char
        idx += 1

    return modified_word

def to_weird_case(string):
    words = string.split()
    idx = 1
    modified_words = []
    for word in words:
        if idx % 3 == 0:
            word = capitalize_second_character(word)
        modified_words.append(word)
        idx += 1
    
    return ' '.join(modified_words)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

