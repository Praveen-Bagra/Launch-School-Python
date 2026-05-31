# input: string containing zero or more space seperated words.
# output: new dictionary
# rules:
#   Explicit:
#       - To return a dictionary. The element of the dictionary
#         should be length of the word: number of such words in an
#         original string.
#       - words consist of any sequence of non-space characters.
#         And to exclude non-letters when determining word size
#         For example 'fiddle!' length is 6
#                     "w@ll" length is 3, "What's" length is 5
#   Implicit:
#       - Empty string should return empty dictionary.
# Test Cases/ Examples: 
#   string = 'Four score and seven.'
#   print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

#   string = 'Hey diddle diddle, the cat and the fiddle!'
#   print(word_sizes(string) == {3: 5, 6: 3})

#   string = 'Humpty Dumpty sat on a w@ll'
#   print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

#   string = "What's up doc?"
#   print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

#   print(word_sizes('') == {})
# Data Structure / Algorithm:
#   - Initialize variable counts to empty dictionary.
#   - Initialize variable words to:
#       split word/s by spaces in a sring and store them
#       in a list.
#   - Iterate over each word in words
#       - Initialize cleaned_word to empty string
#       - Iterate over each character in a word
#           - If it is letter
#               - add it to cleaned_word 
#       - word_length = length of the cleaned_word
#       - if word_length is equal 0, continue to next iteration. 
#       - If word_length alredy there in counts:
#           - Increase its value by one
#       - else
#           - add word_lenght = 1 to the counts dictionary.
#   - Return counts

def word_sizes(string):
    counts = {}
    words = string.split()

    for word in words:
        cleaned_word = ''
        for character in word:
            if character.isalpha():
                cleaned_word += character
        
        word_length = len(cleaned_word)
        if word_length == 0:
            continue 
        
        if word_length in counts:
            counts[word_length] += 1
        else:
            counts[word_length] = 1

    return counts
        
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

string = "What's !!"
print(word_sizes(string) == {5: 1})

print(word_sizes('') == {})
        