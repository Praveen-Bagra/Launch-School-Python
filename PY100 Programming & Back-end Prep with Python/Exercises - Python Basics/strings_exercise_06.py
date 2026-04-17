def is_empty(sentence):
    # return sentence == ''
    # return len(sentence) == 0
    return not sentence


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True