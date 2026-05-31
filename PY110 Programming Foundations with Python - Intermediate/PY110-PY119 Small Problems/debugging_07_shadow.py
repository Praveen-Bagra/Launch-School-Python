def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)

# We are naming the function 'sum'. And we also want to use the 
# built in function sum on list. The funciton sum on line 2 is the same
# function that we have defined, expecting two arguments. It shadowed
# the built in function 'sum'.