my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

def word_length(word):
    return len(word)

odd_words_and_length= { word: word_length(word)
                        for word in my_set
                        if word_length(word) % 2 != 0 }

print(odd_words_and_length)