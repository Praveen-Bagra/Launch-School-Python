string = 'abc def'
my_tuple = ('xyz', 'ghi', 'def')

def ends_with(sentence, substring_tuple):
    for substring in substring_tuple:
        if sentence[len(sentence)-3: len(sentence)] == substring:
            return True
    return False

print(string.endswith(my_tuple))
print(ends_with(string, my_tuple))

string = 'abc lmn'
my_tuple = ('xyz', 'ghi', 'def')

print(string.endswith(my_tuple))
print(ends_with(string, my_tuple))