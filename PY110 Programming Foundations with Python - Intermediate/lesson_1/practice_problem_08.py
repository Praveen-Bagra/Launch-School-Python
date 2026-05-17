statement = "The Flintstones Rock"
letter_with_frequency = {}
for letter in statement:
    if letter == ' ':
        continue
    # letter_with_frequency.setdefault(letter, 0)
    # letter_with_frequency[letter] += 1
    letter_with_frequency[letter] = letter_with_frequency.get(letter, 0) + 1

print(letter_with_frequency)