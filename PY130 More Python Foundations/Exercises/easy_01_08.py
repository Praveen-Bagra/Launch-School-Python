string = 'hello'

reversed_genertor = (char for char in string[::-1])

for char in reversed_genertor:
    print(char)

string = "Hello"

reverse_generator = (string[i] for i in range(len(string) - 1, -1, -1))

for char in reverse_generator:
    print(char)