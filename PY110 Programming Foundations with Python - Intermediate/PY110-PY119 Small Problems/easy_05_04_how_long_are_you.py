# input: string
# output: list of strings
# rules:
#   Explicit:
#       - Return a list containing every word from the string and
#         each word followed by a space and the word's length
#       - Words will be seperated by single space.
#       - It argument is empty string or no argument is passed, it 
#         should return empty list.
# Test Cases / Examples:
# All of these examples should print True
#   words = 'cow sheep chicken'
#   expected_result = ['cow 3', 'sheep 5', 'chicken 7']
#   print(word_lengths(words) == expected_result)        # True

#   words = 'baseball hot dogs and apple pie'
#   expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   #    'and 3', 'apple 5', 'pie 3']
#   print(word_lengths(words) == expected_result)        # True

#   words = "It ain't easy, is it?"
#   expected_result = ['It 2', "ain't 5", 'easy, 5',
                   #    'is 2', 'it? 3']
#   print(word_lengths(words) == expected_result)        # True

#   big_word = 'Supercalifragilisticexpialidocious'
#   print(word_lengths(big_word) == [f'{big_word} 34'])  # True

#   print(word_lengths('') == [])                        # True
#   print(word_lengths() == [])                          # True
# Data Structure and Algorithm:
#   - Initialize variable words to:
#     Split the string into words and return them in a list.
#   - Initialize variable words_length to empty list.
#   - Iterate over each word in words:
#       - Initialize word_length = length of the word
#       - Initialize modified_word = word + ' ' + word_length
#       - Add modified_word to words_length list.
#   - Return words_length list

def word_lengths(string=''):
    # words = string.split()
    # words_length = []
    # for word in words:
        # word_length = len(word)
        # modified_word = word + ' ' + str(word_length)
        # words_length.append(modified_word)

    # return words_length
    if not string:
        return []
    
    return [f'{word} {len(word)}' for word in string.split()]

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True