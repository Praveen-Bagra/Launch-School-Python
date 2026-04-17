def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
# Again it won't print anything. It will return None. 'print(words)' in 
# function body is after the line 'return'. So python will run the 'return'
# statement and will exit immediately. It won't run 'print(words)'.