def mystery(x):
    a = [0, 4, 0, 3, 2]
    while x > 0:
        x = a[x]
        print(x)
    return "Done"

print(mystery(2))
