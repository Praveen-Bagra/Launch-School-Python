import pdb

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

# def is_an_ip_number(num_str):
    # try:
        # number = int(num_str)
        # return number in range(0,256)
    # except ValueError:
        # return False

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

print(is_dot_separated_ip_address('4.5.5'))
print(is_dot_separated_ip_address('1.2.3.4.5'))
print(is_dot_separated_ip_address('0.454.123.-4546'))
print(is_dot_separated_ip_address('1.12.256.123'))
print(is_dot_separated_ip_address('233.145.121.222'))
print(is_dot_separated_ip_address('asdf.12,152.45'))