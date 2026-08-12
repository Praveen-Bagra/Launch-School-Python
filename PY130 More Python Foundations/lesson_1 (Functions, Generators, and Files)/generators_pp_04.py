def capitalized_strings(strings):
    for string in strings:
        yield string.capitalize()

strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
print(tuple(capitalized_strings(strings)))