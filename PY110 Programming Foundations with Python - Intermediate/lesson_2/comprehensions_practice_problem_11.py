dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = [char
                  for inner_lst in dict1.values()
                  for string in inner_lst
                  for char in string
                  if char in 'aeiou']

print(list_of_vowels)

list_of_vowels = []

for inner_lst in dict1.values():
    for string in inner_lst:
        for char in string:
            if char in 'aeiou':
                list_of_vowels.append(char)

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']