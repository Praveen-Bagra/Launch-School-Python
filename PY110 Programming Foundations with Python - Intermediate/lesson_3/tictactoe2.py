# input: lst, strings as delimiters. strings has default values.
# output: string
# rules:
#   Explicit:
#       1. To join elements with delimiter1, and the last element will
#          will be joined by delimiter2 and return a string
#   Implicit:
#       1. If the list is empty, return empty string.
#       2. If the list has two elements, return first element + space + 
#          delimiter2 + space + second element
#       3. If the list has more than two elements, join all the elements
#          except last element with delimiter1. And then join this and
#          last element as per point 2 above.
# Test Cases:
    # print(join_or([1, 2, 3]))               # => "1, 2, or 3"
    # print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
    # print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
    # print(join_or([]))                      # => ""
    # print(join_or([5]))                     # => "5"
    # print(join_or([1, 2]))                  # => "1 or 2"
# Data Structure and Algorithm:
#   - If list has no element:
#       return empty string
#   - if it has one element:
#       return that element as string
#   - if it has two elements:
#       return "first_element delimiter2 second_element" 
#   - if it has more than two elements:
#       - Initialize new_string variable to empty string.
#       - Join all the elements of the list excpet last element with
#           delimiter1, return it as a string
#       - Return the joined string of above string plus delimiter2 plus
#           original list last element

def join_or(lst, delimiter1=', ', delimiter2='or'):
    if len(lst) == 0:
        return ''
    elif len(lst) == 1:
        return f'{lst[0]}' 
    elif len(lst) == 2:
        return f'{lst[0]} {delimiter2} {lst[1]}'
    else:
        new_string = ''
        for element in lst[:-1]:
            new_string += str(element) + delimiter1
        return f'{new_string}{delimiter2} {lst[-1]}'
    
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

# If there is HUMAN_MARKER in any 2 positions in winning line and 
# 3rd position is empty then computer should choose that positing
# otherwise it can choose any empty position.

