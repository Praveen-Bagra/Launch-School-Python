# input: string
# output: Boolean True or False
# rules
#   Explicit
#       - Returns True if the string is a pangram, False
#         otherwise.
#       - Pangrams are sentences that contain every letter
#         of the alphabet at least once.
#       - alphabet case is insensitive. So "A" is equal to
#         'a'
# 
# Test Cases and Examples.
#   print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
#   print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
#   print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
#   print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
#   print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)
#   my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
#   print(is_pangram(my_str) == True)

# Data Structure and Algorithm

    # - Initialize alphabets to list to ['a', 'b', 'c'...'z']
    # - Iterate over each character in string.
        # - if char converted to lowercase in alphabets
            # - remove char from alphabets

    # - if alphabets is empty:
        # - Return True
    # - Return False

def is_pangram(string):
    alphabets =list('abcdefghijklmnopqrstuvwxyz')
    for char in string:
        char = char.casefold()
        if char in alphabets:
            alphabets.remove(char)

    if alphabets == []:
        return True
    
    return False

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
