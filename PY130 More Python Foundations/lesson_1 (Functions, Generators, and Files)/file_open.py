# file = open('example.txt', 'r')
# content = file.read()
# file.close()

# print(repr(content))

# file = open('example.txt', 'r')
# content = file.readlines()
# file.close()

# print(repr(content))

# file = open('example.txt', 'r')
# print(repr(file.readline()))
# print(repr(file.readline()))
# print(repr(file.readline()))
# print(repr(file.readline()))
# print(repr(file.readline()))
# print(repr(file.readline()))
# file.close()

file = open('example.txt', 'r')
for line in file:
    print(repr(line))