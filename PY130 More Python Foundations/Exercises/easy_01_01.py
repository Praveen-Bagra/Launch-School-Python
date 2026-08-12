# lst = [1, 2, 3, 4, 5]
# squared_list = list(map(lambda num: num**2, lst))
# print(squared_list)

lst = [1, 2, 3, 4, 5]
def square(num):
    return num**2

squared_list = list(map(square, lst))
print(squared_list)