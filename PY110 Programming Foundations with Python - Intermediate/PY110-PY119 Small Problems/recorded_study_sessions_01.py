target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

# Data Structure and Algorithm:
#   - Initialize variable 'letters_count' to empty dictionary
#   - Iterate over each target letter
#       - Initialize variable count to:
#           count target letter in characters
#       - Initialize variable present to False
#       - If count is greater than 0:
#           reassign the present to True
#       - Add target letter: {'present': present, 'count': count}
#         to letters_count dictionary.
#   - Print letters_count dictionary.

letters_count = {}
for target_letter in target_letters:
    count = characters.count(target_letter)
    present = False
    if count > 0:
        present = True
    letters_count[target_letter] = {'present': present, 'count': count}

print(letters_count)

letters_count = {target_letter: {'present': (True if target_letter in characters else False),
                                 'count': characters.count(target_letter)}
                 for target_letter in target_letters}

print(letters_count)