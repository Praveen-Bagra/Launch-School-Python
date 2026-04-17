str = 'launch school tech & talk'
print(str.title())

result = []
for word in str.split():
    result.append(word.capitalize()) 

print(' '.join(result))
