import re

# No /(ABC|abc)/ and /[Aa][Bb][Cc] are different. The first pattern will
# match only two patterns i.e. ABC or abc. While the second pattern will
# match multiple patterns i.e. Abc or aBc or ABC or abc.

string = 'Abc'


print(re.search(r'(ABC|abc)', string)) # None
print(re.search(r'[Aa][Bb][Cc]', string))  # Returned match object.