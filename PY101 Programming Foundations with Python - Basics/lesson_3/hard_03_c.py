def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # Prints one is: ['two']
print(f"two is: {two}") # Prints two is: ['three']
print(f"three is: {three}") # Prints three is: ['one']