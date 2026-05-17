def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # Prints one is: ["one"]
print(f"two is: {two}") # Prints two is: ["two"]
print(f"three is: {three}") # Prints three is: ["three"]