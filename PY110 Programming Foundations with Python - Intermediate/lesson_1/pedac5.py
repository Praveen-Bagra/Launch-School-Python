# input: a list of strings
# output: a same list sorted according to the highest number of adjacent
#         consonants.
# rules:
#   Explicit:
#       1. Sort the list based on the highest number of adjacent
#          consonants.
#       2. If two strings have same adjacent consonants, they should
#          appear in the same order to relation to each other.
#       3. Consonants are adjacent if they are next to each other in the
#          same word or there is a space between two consonants in the
#          adjacent word.
#       4. adjacent
#   Implicit:
#       Assuming adjacent consonants are case sensitive.
# Test Cases:
    # my_list = ['aa', 'baa', 'ccaa', 'dddaa']
    #              0 ,   0   ,  2    ,  3
    # print(sort_by_consonant_count(my_list))
    # # ['dddaa', 'ccaa', 'aa', 'baa']

    # my_list = ['can can', 'toucan', 'batman', 'salt pan']
    #               2      ,   0     ,  2     ,   3
    # print(sort_by_consonant_count(my_list))
    # # ['salt pan', 'can can', 'batman', 'toucan']

    # my_list = ['bar', 'car', 'far', 'jar']
    #              0  ,   0  ,   0   ,  0
    # print(sort_by_consonant_count(my_list))
    # # ['bar', 'car', 'far', 'jar']

    # my_list = ['day', 'week', 'month', 'year']
    #              0   ,  0   ,    3    ,  0
    # print(sort_by_consonant_count(my_list))
    # # ['month', 'day', 'week', 'year']

    # my_list = ['xxxa', 'xxxx', 'xxxb']
    # print(sort_by_consonant_count(my_list))
    # # ['xxxx', 'xxxb', 'xxxa']

    # my_list = ['rstafgdjecc', 'bcdfg', 'abcd febciajkl']
    #                   4     ,    5   ,    4
    # print(sort_by_consonant_count(my_list))
    # ['bcdfg', 'rstafgdfecc', 'abcd febciajkl']
# Data Structure and Algorithm:
#   - Return a new sorted list based on the function defined below.
#   - Fuction : Return highest number of adjacent consonants in a string.
#       a. Declare total variable and initialize to 0.
#       b. Declare consonants variable to characters 'a' to 'z' 
#          except a, e, i, o, u
#       c. Declare current_idx variable and initialize to 0
#       d. While current_idx is less than equal to length of the string - 2:
#           next_character_idx = current_idx + 1
#           if string[next_character_idx] == ' ':
#               next_character_idx = current_idx + 2
#           if string[current_idx] in consonants and
#               string[next_character_idx] in consonants:
#                   if total is equal to 0
#                       total += 2
#                   else:
#                       total += 1
#           current_idx += 1
#       e. Return total

# Data Structure and Algorithm:
#   - Return a same sorted list based on the function defined below.
#   - Fuction : Return highest number of adjacent consonants in a string.
#       a. Declare adjacent_consonants variable and initialize to empty list. 
#          And max_adjacent_consonants variable & initialize to 0.
#       b. Declare consonants variable to characters 'a' to 'z' 
#          except a, e, i, o, u
#       c. Declare current_idx variable and initialize to 0.
#       d. While current_idx is less than equal to length of the string - 2:
#           next_character_idx = current_idx + 1
#           if string[next_character_idx] == ' ':
#               next_character_idx = current_idx + 2
#           if string[current_idx] in consonants and
#               string[next_character_idx] in consonants:
#                   if adjacent_consonants == []
#                       adjacent_consonants.append(string[current_idx])
#                       adjacent_consonants.append(string[next_character_idx])
#                       if max_adjacent_consonants > len(adjacent_consonants):
#                           max_adjacent_consonants = len(adjacent_consonants)
#                   else:
#                       adjacent_consonants.append(string[next_character_idx])
#                       if max_adjacent_consonants > len(adjacent_consonants):
#                           max_adjacent_consonants = len(adjacent_consonants)
#           else:
#               if max_adjacent_consonants > len(adjacent_consonants):
#                   max_adjacent_consonants = len(adjacent_consonants)
#                   adjacent_consonants = []
#           current_idx += 1
#       e. Return max_adjacent_consonants


def total_adjacent_consonants(string):
    total = 0
    consonants = ['b', 'c', 'd', 'f',
                  'g', 'h', 'j', 'k', 
                  'l', 'm', 'n', 'p', 
                  'q', 'r', 's', 't', 
                  'v', 'w', 'x', 'y', 
                  'z',
    ]
    current_idx = 0
    while current_idx <= (len(string) - 2):
        next_character_idx = current_idx + 1
        if string[next_character_idx] == ' ':
            next_character_idx = current_idx + 2
        if ((string[current_idx] in consonants) and
              (string[next_character_idx] in consonants)):
            if total == 0:
                total += 2
            else:
                total += 1
        current_idx += 1

    return total

def max_adjacent_consonants_count(string):
    adjacent_consonants = []
    max_adjacent_consonants = 0
    consonants = ['b', 'c', 'd', 'f',
                  'g', 'h', 'j', 'k', 
                  'l', 'm', 'n', 'p', 
                  'q', 'r', 's', 't', 
                  'v', 'w', 'x', 'y', 
                  'z',
    ]
    current_idx = 0
    while current_idx <= (len(string) - 2):
        current_character = string[current_idx]
        next_character = string[current_idx + 1]
        if next_character == ' ':
            next_character = string[current_idx + 2]

        if ((current_character in consonants) and 
        (next_character in consonants)):
            if adjacent_consonants == []:
                adjacent_consonants.append(current_character)
                adjacent_consonants.append(next_character)
                if max_adjacent_consonants < len(adjacent_consonants):
                    max_adjacent_consonants = len(adjacent_consonants)
            else:
                adjacent_consonants.append(next_character)
                if max_adjacent_consonants < len(adjacent_consonants):
                    max_adjacent_consonants = len(adjacent_consonants)
        else:
            if max_adjacent_consonants < len(adjacent_consonants):
                max_adjacent_consonants = len(adjacent_consonants)
            adjacent_consonants = []
        current_idx += 1
    
    return max_adjacent_consonants



def sort_by_consonant_count(lst):
    lst.sort(key=max_adjacent_consonants_count, reverse=True)
    return lst

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

my_list = ['rstafgdjecc', 'bcdfg', 'abcd febciajkl']
print(sort_by_consonant_count(my_list))
# ['bcdfg', 'rstafgdfecc', 'abcd febciajkl']

# print(total_adjacent_consonants('salt pan'))
# print(total_adjacent_consonants('rstafgdjecc'))

# print(max_adjacent_consonants_count('rstafgdjecc')) # 4
# print(max_adjacent_consonants_count('bcdfg')) # 5
# print(max_adjacent_consonants_count('abcd febciajkl')) # 4
# print(max_adjacent_consonants_count('ccaa')) # 2
# print(max_adjacent_consonants_count('bar')) # 0


