def hello():
    print('Hello')

hi = hello

hello()
hi()
print()

def i_have_such_a_long_and_annyoying_name(value):
    print(value)

too_long = i_have_such_a_long_and_annyoying_name
too_long('Some text')
too_long(3.141592)
too_long('Some text' == 3.141592)