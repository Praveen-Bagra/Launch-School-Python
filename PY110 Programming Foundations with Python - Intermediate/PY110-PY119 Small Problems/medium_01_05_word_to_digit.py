# input: string
# output: string
# rules:
#   Explicit:
#       - Return a string with every occurence of a 'number word'
#         converted to its corresponding digit character.
#       - String will not contain any punctuation.
#   Implicit:
#       - Words are seperated by single whitespace.
# Test Cases / Examples:
#   message = 'Please call me at five five five one two three four'
#   print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
#   # Should print True
# Data Structure and Algorithm:
#   - Initialize num_words to:
#       {'one': '1', 'two': '2'...upto 'zero': '0'}
#   - Initialize variable 'words' to:
#     split the sentence into words and return them in a list.
#   - Initialize 'modified_words' to empty list
#   - Iterate for each word in words
#       - If word is in num_words
#           - word = associated value from num_words
#       - Add word to modified_words
#   - Return modified_words joined with single whitespace as string.

def word_to_digit(sentence):
    num_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9', 'zero': '0'}
    words = sentence.split()
    modified_words = []
    for word in words:
        if word in num_words:
            word = num_words[word]
            
        modified_words.append(word)
    
    return ' '.join(modified_words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True