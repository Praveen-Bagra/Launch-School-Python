def reverse_string(string):
    new_string = ''
    for char in string:
        new_string = char + new_string

    return new_string

print(reverse_string("hello")) # == "olleh")

# We are reassigning variable string during each iteration.
# It will iterate five times:
# 1st iteration: string = hhello
# 2nd iteration: string = ehhello
# 3rd iteration: string = lehhello
# 4th iteration: string = llehhello
# 5th iteration: string = ollehhello
# It returns ollehhello