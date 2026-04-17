print('johnson' in 'Joe Johnson') # Prints False
print('sen' not in 'Joe Johnson') # Prints True
print('Joe J' in 'Joe Johnson') # Prints True
print(5 in range(5)) # Prints False
print(5 in range(6)) # Prints True
print(5 not in range(5, 10)) # Prints False
print(0 in range(10, 0, -1)) # Prints False
print(4 in {6, 5, 4, 3, 2, 1}) # Prints True
print({1, 2, 3} in {1, 2, 3}) # Prints False
print({3, 2} in {1, frozenset({2, 3})}) # Prints True