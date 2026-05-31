# input: dictionary
# output: new dictionary
# rules
#   Explicit: 
#       - Retunrs a dictionary by inverting it. Meaning its keys
#         should become values and values should become keys.
#       - Key and values are unique.
# Examples / Test Cases:
#   print(invert_dict({
          # 'apple': 'fruit',
          # 'broccoli': 'vegetable',
          # 'salmon': 'fish',
      # }) == {
          # 'fruit': 'apple',
          # 'vegetable': 'broccoli',
          # 'fish': 'salmon',
      # })  # True
# Data Structure and Algorithm:
#   - Intialize variable invert_dict to empty dictionary.
#   - Iterate over key, value pair in dictionary
#       Add value as key and key as value in invert_dict
#   - Return invert_dict


def invert_dict(dictionary):
#     invert_dict = {}
    # for key, value in dictionary.items():
        # invert_dict[value] = key

    # return invert_dict

    return {value: key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True