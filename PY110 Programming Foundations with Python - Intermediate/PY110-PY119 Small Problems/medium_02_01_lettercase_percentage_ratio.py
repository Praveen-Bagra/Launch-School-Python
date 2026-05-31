# input: string
# output: dictionary
# rules:
#   - Returns a dictionary containing the followring three properties
#       - {'lowercase': 'lowercase_percentage',
#           'uppercase': 'uppercase_percentage',
#           'neither': 'neither_percentage'}
#   - percentages should be returned as strings whose numeric values
#     lies between '0.00; and '100.00'. Each value should be rounded
#     to two decimal points.
# Test Cases / Examples
#   expected_result = {
    #   'lowercase': "50.00",
    #   'uppercase': "10.00",
    #   'neither': "40.00",
#   }
#   print(letter_percentages('abCdef 123') == expected_result)

#   expected_result = {
    #   'lowercase': "37.50",
    #   'uppercase': "37.50",
    #   'neither': "25.00",
#   }
#   print(letter_percentages('AbCd +Ef') == expected_result)

#   expected_result = {
    #   'lowercase': "0.00",
    #   'uppercase': "0.00",
    #   'neither': "100.00",
#   }
#   print(letter_percentages('123') == expected_result)
# Data Structure and Algorithm:
#   - Initialize case_and_counts to:
#       {'lowercase': 0, 'uppercase': 0, 'neither': 0}
#   - Iterate over each char in string
#       - if case is lowercase:
#           - increase 'lowercase' value by 1 in case_and_counts
#       - is case is uppercase:
#           - increase 'lowercase' value by 1 in case_and_counts
#       - else
#           - increase 'neither' value by 1 in case_and_counts
#   - initialize total_char = total chars in string
#   - initialize lowercase_percentage = lowercase value in case_and_counts/
#                                       total chars. Make it rounded to 2
#   - Do the simlar for uppercase and neither case
#   - Initialize case_and_percentage to:
#       {'lowercase': lowercase_percentage converted to string...}
#   - return case_and_percentage

def letter_percentages(string):
    case_and_counts = {'lowercase': 0, 'uppercase': 0, 'neither': 0}
    for char in string:
        if char.islower():
            case_and_counts['lowercase'] += 1
        elif char.isupper():
            case_and_counts['uppercase'] += 1
        else:
            case_and_counts['neither'] += 1
    
    total_chars = len(string)
    lowercase_percentage = round((case_and_counts['lowercase'] / total_chars) * 100, 2)
    uppercase_percentage = round((case_and_counts['uppercase'] / total_chars) * 100, 2)
    neither_percentage = round((case_and_counts['neither'] / total_chars) * 100, 2)

    case_and_percentage = {'lowercase': f'{lowercase_percentage:.2f}',
                           'uppercase':f'{uppercase_percentage:.2f}',
                           'neither': f'{neither_percentage:.2f}'}

    return case_and_percentage

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123')) # == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
