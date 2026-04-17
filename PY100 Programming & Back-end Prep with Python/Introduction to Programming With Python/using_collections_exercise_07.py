info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# result = ''
# for char in info:
    # if char == ':':
        # result += '+'
    # else:
        # result += char
words_list = info.split(':')
result = '+'.join(words_list)

print(result)
print(info.replace(':', '+'))