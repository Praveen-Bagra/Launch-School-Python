# - Initalize LETTERS to 'ABC....Z'
# - Initialize variable initial_space to find index of input letter in LETTERS
# - Initialize middle space to 1
# - Initialize letter to None 
# - Iterate over the letters:
#       - If input_letter is 'A'
#               - print letter
#               - break   
#       - else
#               - print initial_space + current_letter + middle_space 
#                 + current_letter
#               - decrease initial_space by 1
#               - increase middle_space by 2
#
#       - Reassign letter to current_letter
#       - If letter is equal to input letter:
#           - break

# - Iterate over the letters in reverse:
#       - If input_letter is 'A':
#           - break
#       - If ord(current_letter) < ord(letter):
#               - If current_letter is A:
#                   - increase initial_space by 1
#                   - print initial_space + letter
#               - else:
#                   - increase initial_space by 1
#                   - decrease middle_space by 2
#                   - print initial_space current_letter middle_space 
#                     current_letter

class Diamond:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def make_diamond(cls, character):
        initial_space = Diamond.LETTERS.index(character)
        middle_space = 0
        letter = None
        result = []

        for current_letter in Diamond.LETTERS:
            if character == 'A':
                result.append(current_letter + '\n')
                break

            if current_letter == 'A':
                result.append((' ' * initial_space) + 'A' 
                                + (' ' * initial_space) + '\n')
            else:
                initial_space -= 1
                if middle_space == 0:
                    middle_space += 1
                else:
                    middle_space += 2

                result.append((' ' * initial_space) + current_letter 
                                + (' ' * middle_space) + current_letter
                                + (' ' * initial_space) + '\n')

            letter = current_letter
            if letter == character:
                break

        for current_letter in reversed(Diamond.LETTERS):
            if character == 'A':
                break

            if ord(current_letter) < ord(letter):
                if current_letter == 'A':
                    initial_space += 1
                    result.append((' ' * initial_space) + current_letter
                                    + (' ' * initial_space) + '\n')
                else:
                    initial_space += 1
                    middle_space -= 2
                    result.append((' ' * initial_space) + current_letter 
                            + (' ' * middle_space) + current_letter
                            + (' ' * initial_space) + '\n')

        return ''.join(result)





