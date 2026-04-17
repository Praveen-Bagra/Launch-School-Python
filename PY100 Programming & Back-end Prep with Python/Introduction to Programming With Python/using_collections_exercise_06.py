print('abc-def'.isalpha()) # Prints False
print('abc_def'.isalpha()) # Prints False
print('abc def'.isalpha()) # Prints False
print('abc def'.isalpha() and # Prints False
      'abc def'.isspace())
print('abc def'.isalpha() or # Prints False
      'abc def'.isspace())
print('abcdef'.isalpha()) # Prints True
print('31415'.isdigit()) # Prints True
print('-31415'.isdigit()) # Prints False
print('31_415'.isdigit()) # Prints False
print('3.1415'.isdigit()) # Prints False
print(''.isspace()) # Prints False
