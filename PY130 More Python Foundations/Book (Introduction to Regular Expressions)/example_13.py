import re
string = 'xabcbcbacy'
print(re.findall(r'a[abc]*c', string))
print(re.findall(r'a[abc]*?c', string))
