# input: string containing zero or more space seperated words.
# output: new dictionary
# rules:
#   Explicit:
#       - To return a dictionary. The element of the dictionary
#         should be length of the word: number of such words in an
#         original string.
#       - words consist of any sequence of non-space characters.
#         For example 'diddle,', 'diddle!', "What's", 'doc?' are all
#         considered one word.
#   Implicit:
#       - Empty string should return empty dictionary.
# Test Cases / Examples:
#   string = 'Four score and seven.'
#   print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

#   string = 'Hey diddle diddle, the cat and the fiddle!'
#   print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

#   string = 'Humpty Dumpty sat on a wall'
#   print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

#   string = "What's up doc?"
#   print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

#   print(word_sizes('') == {})
# Data Structure / Algorithm:
#   - Initialize variable result_dict to empty dictionary.
#   - Initialize variable words to:
#       Split the words by spaces in original stirng and return them
#       in a list. 
#   - Iterate over each word in words list
#       word_length = length of the word
#       If word_length key is already in dictionary
#           Increase its value by 1
#       else
#           add word_length as key and value as 1
#   - return result_dict

def word_sizes(string):
    result_dict = {}
    words = string.split()

    for word in words:
        word_length = len(word)
        if word_length in result_dict:
            result_dict[word_length] += 1
        else:
            result_dict[word_length] = 1
    
    return result_dict

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string)  == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})