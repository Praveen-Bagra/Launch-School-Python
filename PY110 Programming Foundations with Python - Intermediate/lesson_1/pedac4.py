# input: Integer (number of blocks)
# output: Integer (leftover blocks after building the tallest possible
#           valid structure)
# rules:
#   Explicit:
#       1. The top layer is a single block.
#       2. The structure is built in layers.
#       3. The single block should contain contain four blocks in lower
#          layer to support it.
#       4. A block in lower layer can support any number of blocks in 
#          upper layer.
#       5. There is no gap between blocks
#   Implicit:
#       1. If block is represented by 'O'. the structure will look like:
#           O : 1 * 1
#           OO OO : 2 * 2
#           OOO OOO OOO : 3 * 3
#           0000 0000 0000 0000 : 4 * 4 
#           ...
# Test Cases / Examples
#   print(calculate_leftover_blocks(0) == 0)  # True
#   print(calculate_leftover_blocks(1) == 0)  # True
#   print(calculate_leftover_blocks(2) == 1)  # True
#   print(calculate_leftover_blocks(4) == 3)  # True
#   print(calculate_leftover_blocks(5) == 0)  # True
#   print(calculate_leftover_blocks(6) == 1)  # True
#   print(calculate_leftover_blocks(14) == 0) # True
# Data Structure / Algorithm:
#   - Declare result variable and initialize it to empty list.
#   - Declare layer variable to 1
#   - Iterate till sum of the result list is less than equal to the input blocks:
#       - current_num = layer * layer
#       - append current_num to list
#       - layer += 1
#   - Remove the last element of the result list.
#   - Return blocks - sum of result list.

def calculate_leftover_blocks(blocks):
    result = []
    current_layer = 0
    while sum(result) <= blocks:
        current_num = current_layer * current_layer
        result.append(current_num)
        current_layer += 1

    result.pop()
    return blocks - sum(result)


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True