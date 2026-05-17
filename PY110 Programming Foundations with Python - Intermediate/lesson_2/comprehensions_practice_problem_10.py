import random

def return_uuid():
    characters ='abcdef0123456789'
    uuid = ''
    iteration_times = [8, 4, 4, 4, 12]

    for num in iteration_times:
        for _ in range(num):
            uuid += random.choice(characters)
        uuid += '-'
    uuid = uuid.rstrip('-')
    
    return uuid
    
print(return_uuid())

def generate_uuid():
    hex_chars = 'abcdef0123456789'
    uuid = []
    sections = [8, 4, 4, 4, 12]

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

print(generate_uuid())

