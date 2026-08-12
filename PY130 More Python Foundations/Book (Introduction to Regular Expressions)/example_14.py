import re

text = 'Four score and seven'

vowelless = re.sub(r'[aeiou]', '*', text)
print(vowelless)

first_3 = re.sub(r'[aeiou]', '*', text, count=3)
print(first_3)