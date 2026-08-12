def capitalized(strings):
    for string in strings:
        if len(string) < 5:
            yield string.capitalize()

strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
print(set(capitalized(strings)))