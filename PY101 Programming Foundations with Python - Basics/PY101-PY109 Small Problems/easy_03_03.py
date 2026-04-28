# input: string
# output: Print string. Overall print argument in a box. Box is also a 
#         string.
# Test cases:
#   print_in_box('To boldly go where no one has gone before.')
#   +--------------------------------------------+
#   |                                            |
#   | To boldly go where no one has gone before. |
#   |                                            |
#   +--------------------------------------------+
#   print_in_box('')
#   +--+
#   |  |
#   |  |
#   |  |
#   +--+
# Data Structure and Algorithm:
#   a. initialize length = length of the string.
#   b. print + & (- * length + 2) & +
#      print | & (space * lenght + 2) & |
#      print | & space & string & space & |
#      print | & (space * lenght + 2) & |
#      print + & (- * length + 2) & +

def print_in_box(string):
    length = len(string)
    print(f'+{'-' * (length + 2)}+')
    print(f'|{' ' * (length + 2)}|')
    print(f'| {string} |')
    print(f'|{' ' * (length + 2)}|')
    print(f'+{'-' * (length + 2)}+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')