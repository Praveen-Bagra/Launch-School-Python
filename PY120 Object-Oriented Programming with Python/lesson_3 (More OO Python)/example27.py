def convert_to_integer(value):
    try:
        return int(value)
    except ValueError as e:
        raise TypeError('Expected a numeric string') from e

try:
    convert_to_integer('abc')
except TypeError as error:
    print(f'Error: {error}')
    print(f'Original error: {error.__cause__}')