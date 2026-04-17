def is_empty_or_blank(s):
    # return not s or s.isspace()
    return not s.strip(' ') 

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

