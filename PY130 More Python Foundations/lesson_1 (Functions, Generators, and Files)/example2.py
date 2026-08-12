with open('myfile.txt', 'r') as file:
    for line in file:
        print(line.upper())

with open('myfile.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.upper())

with open('myfile.txt', 'r') as file:
    content = file.read()

print(content)