input_str = input()
str_length = len(input_str)
first_character = input_str[0]
last_character = input_str[str_length-1]
if str_length == 3:
   remaining_characters = input_str[1]
if str_length > 3:
    remaining_characters = input_str[1:(str_length-1)]
if str_length == 2:
   result = last_character + first_character
if str_length > 2:
    result = last_character + remaining_characters + first_character
print(result)