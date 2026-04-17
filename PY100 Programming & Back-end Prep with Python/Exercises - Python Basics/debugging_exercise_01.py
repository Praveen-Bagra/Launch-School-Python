def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# print(find_first_nonzero_among([0, 0, 1, 0, 2, 0]))
# print(find_first_nonzero_among([1]))

# On line 6 we have provided 6 arguments instead of 1 iterable. 
# On line 7, we have provided int object. We have to provide 1 iterable
# instead.