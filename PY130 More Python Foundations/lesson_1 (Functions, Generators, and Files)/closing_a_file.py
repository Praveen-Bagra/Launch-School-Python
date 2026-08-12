file = open('output.txt', 'w')
file.write('Hello, world!\n')

lines = ['Firstline\n', 'Second line\n']
file.writelines(lines)
file.close()