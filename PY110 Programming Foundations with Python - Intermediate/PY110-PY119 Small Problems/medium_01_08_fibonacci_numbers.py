def fibonacci(nth):
    if nth in [1, 2]:
        return 1

    return fibonacci(nth - 1) + fibonacci(nth - 2)

    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]



print(fibonacci(5))
print(fibonacci(8))

# fibonacci(4) + fibonacci(3)
# fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
# fibonacci(2) + fibonacci(1) + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1


# fibonacci(8)
# fibonacci(7) + fibonacci(6)
# fibonacci(6) + fibonacci(5) + fibonacci(5) + fibonacci(4)
# f(5) + f(4) + f(4) + f(3) + f(4) + f(3) + f(3) + f(2)
# f(4) + f(3) + f(3) + f(2) + f(3) + f(2) + f(2) + f(1) + f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + 1
# f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + 1 + f(2) + f(1) + 1 + 1 + 1 + f(2) + f(1) + 1 + 1 + 1 +1 + 1 + 1
# f(2) + f(1) + 1 + 1 + 1+ 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# 1 + 1 + 19

