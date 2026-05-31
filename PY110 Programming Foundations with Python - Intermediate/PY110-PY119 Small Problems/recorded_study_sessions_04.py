# input: string and a list
# output: new list
# rules:
#   Explicit:
#       - Return a new list containing anagrams of a original string.
#       - Anagrams are words having same letters count-wise.
#       - Characters in anagrams are case insensitive. 'racer' is 
#         equal to 'Racer'.
#       - If there are no anagram words, the function should return 
#         empty list.
# Data Structure and Algorithm:
#   - string = string converted to lowercase
#   - Initialize counts as empty dictionary
#   - Iterate through each character in the string
#       - If character is in dictionary:
#           - Increase its associated value by 1
#       - Else
#           - Add character as key and value as 1 in counts.
#   - Intialize anagrams_lst to empty list.
#   - Iterate for each word in the list
#       - Initialize variable 'add_word' to True
#       - Iterate for each character in the word
#           - character = character converted to lowercase
#           - check its count in word, if is not equal to its associated
#             value in counts
#                  - Reassign 'add_word' to False
#                  - break
#       - if add_true is equal to True
#           - add word to anagrams_lst
#   - Return anagrams_list

def anagrams(string, words):
    string = string.casefold()
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    anagrams_lst = []
    for word in words:
        add_word = True
        for char in word:
            char = char.casefold()
            if word.casefold().count(char) != counts.get(char, 0):
                add_word = False
                break
        if add_word == True:
            anagrams_lst.append(word)
    
    return anagrams_lst
            
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'Racer']))
print(anagrams('hello', ['hi', 'how are you']))