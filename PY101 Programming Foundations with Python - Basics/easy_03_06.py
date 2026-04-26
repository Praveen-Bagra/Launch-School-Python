# input: 4 string words
# output: Print story
# Test Caes:
#   Enter a noun: dog
#   Enter a verb: walk
#   Enter an adjective: blue
#   Enter an adverb: quickly
#   Prints:
#   Do you walk your blue dog quickly? That's hilarious!
#   The blue dog walks quickly over the lazy dog.
#   The dog quickly walks up to Joe's blue turtle.
# Data Structure and Algorithm:
#   a. ask for noun, verb, adjective and adverd. Initialize them
#      accordingly.
#   b. print required story containing above variables

noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')

print()
print(f"Do you {verb} your {adjective} {noun} {adverb}? "
      f"That's hilarious!")
print(f'The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.')
print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")