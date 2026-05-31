word = 'what-a-b.e.a.utiful day!'
# crazy_letters = [char for char in word if char.isalpha()]
# print(crazy_letters)

# Data Structure and Algorithm:
#   - Initialize variable crazy_letters to empty list.
#   - Initialize idx equal to 0
#   - Iterate through each character
#       - If char is aplhabet and idx is even
#           - add lowercase char to crazy_letters
#           - add idx value by 1
#       - else char is alphabet and idx is idd
#           - add uppercae char to crazy_letters
#           - add idx value by 1

crazy_letters = []
idx = 0
for char in word:
    if char.isalpha() and idx % 2 == 0:
        crazy_letters.append(char.lower())
        idx += 1
    elif char.isalpha() and idx % 2 == 1:
        crazy_letters.append(char.upper())
        idx += 1

print(crazy_letters)

