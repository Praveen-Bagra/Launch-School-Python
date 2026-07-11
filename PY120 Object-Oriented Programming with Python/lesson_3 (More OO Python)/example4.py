class User:
    def __init__(self, login_name, password):
        self.login_name = login_name
        self._password = password

john = User('john', 'I-yam-what-I-yam.')

print(john._password)
john._password = "May-I-tahw-may-I."
print(john._password)