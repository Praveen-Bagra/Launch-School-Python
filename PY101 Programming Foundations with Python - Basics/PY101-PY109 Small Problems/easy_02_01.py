# input: A name list containing 2 or more elements i.e. first name, 
#        middle name (optional), surname.
#        A dictonary containing two keys i.e. "title" & "occupation"
#        and the appropriate values.
# output: Returns a string i.e. Hello, full name! Nice to have a title 
#         occupation round.
# Test Cases:
#   greetings(
#       ["John", "Q", "Doe"],
#       {"title": "Master", "occupation": "Plumber"},
#       )
#   Returns Hello, John Q Doe! Nice to have a Master Plumber around.
# Data Structure and Algorithm:
#   a. initialize full_name = full name with spaces (' '.join (list))
#   b. initialize title and occupation with dictnary values
#   b. Returns the string with above values.

def greetings(name_list, details_dict):
    full_name = ' '.join(name_list)
    title = details_dict['title']
    occupation = details_dict['occupation']
    return (f'Hello, {full_name}!, Nice to have a {title} '
             f'{occupation} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.