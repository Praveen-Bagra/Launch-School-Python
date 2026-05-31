# input: Dictionary and a List of keys
# ouput: new dictionary
# rules:
#   Explicit:
#       - Return a new dictionary containing key/value pairs of the
#         specified keys.
# Test Cases / Examples:
#   input_dict = {
    #   'red': 1,
    #   'green': 2,
    #   'blue': 3,
    #   'yellow': 4,
#   }

#   keys = ['red', 'blue']
#   expected_dict = {'red': 1, 'blue': 3}
#   print(keep_keys(input_dict, keys) == expected_dict) # True
# Data Structure and Algorithm:
#   - Initialize specified_keys to empty dictionary.
#   - Iterate for each key, value pair in original dictionary
#       - If key is in list value passed as an argument
#           add key, value pair to specified_keys
#   - Return specified_keys

def keep_keys(dictionary, keys):
    # specified_keys = {}
    # for key, value in dictionary.items():
        # if key in keys:
            # specified_keys[key] = value
    
    # return specified_keys

    return {key: value 
            for key, value in dictionary.items()
            if key in keys}
    
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True