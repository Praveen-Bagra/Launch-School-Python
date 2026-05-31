animals = {'cow': 'moo', 'cat': 'meow', 'dog': 'woof'}

# Data Structure and Algorithm:
#   - Initialize variable sounds to empty list.
#   - Iterate ever each value in animals:
#       - add value + '-' + value to sounds
#   - print sounds

def sounds(dictionary):
    # sounds_lst = []
    # for sound in dictionary.values():
        # sounds_lst.append(sound + '-' + sound)

    # return sounds_lst
    return [sound + '-' + sound
            for sound in animals.values()]

print(sounds(animals))


