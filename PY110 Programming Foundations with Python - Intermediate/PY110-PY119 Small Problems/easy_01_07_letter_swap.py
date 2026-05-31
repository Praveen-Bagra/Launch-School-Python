# input: string
# output: string
# rules:
#   Explicit:
#       - Returns a string with first and last letter of every word 
#         swaped.
#       - Words are seperated by spaces.
#       - Every word contains at least one letter.
#       - String will always contain at least word.
#       - String contains nothing but spaces and there are no
#         leading, trailing, repeated spaces.
#   Implicit:
#       - If word contains one character, return that character.
#         For example 'a' should return 'a'.
# Test Cases / Examples:
#   print(swap('Oh what a wonderful day it is')
      # == "hO thaw a londerfuw yad ti si")  # True
#   print(swap('Abcde') == "ebcdA")            # True
#   print(swap('a') == "a")                    # True
# Data Strucute and Algorithm:
#   - Initialize variable words to:
#     list containing words. Words are strings seperated by spaces.
#   - Initialize swapped_words_list to empty list.
#   - Iterate over each word in words:
#       - if word length is 1:
#           swapped_word = word
#       - else
#           swapped_word = word last character + (word second character
#                           to word second last character) + word first
#                           character
#       - add swapped_word to swapped_words_list
#   - Join swapped_words_list words by spaces and return that as
#     string.

def swap(sentence):
    words = sentence.split()
    swapped_words_list = []

    for word in words:
        if len(word) == 1:
            swapped_word = word
        else:
            swapped_word = word[-1] + word[1:-1] + word[0]

        swapped_words_list.append(swapped_word)

    return ' '.join(swapped_words_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True