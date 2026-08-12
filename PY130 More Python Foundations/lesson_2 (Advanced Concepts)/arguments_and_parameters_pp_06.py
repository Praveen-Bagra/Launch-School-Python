def concat_strings(*args, sep=' '):
    return sep.join(args)

print(concat_strings('how', 'are', 'you'))
print(concat_strings('how', 'are', 'you', sep=', '))