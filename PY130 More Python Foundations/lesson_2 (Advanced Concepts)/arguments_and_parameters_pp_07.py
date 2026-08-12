def register(username, /, age, *, password):
    return {
        'username': username,
        'age': age,
        'password': password,
    }

print(register('prvn', 30, password='asdf1234'))
print(register('prvn', age=30, password='asdf1234'))
