def print_message(*, message, level='INFO'):
    print(f'[{level}] {message}')

print_message(message="It's tasty.")
print_message(message="It's not tasty.", level='WARNING')

