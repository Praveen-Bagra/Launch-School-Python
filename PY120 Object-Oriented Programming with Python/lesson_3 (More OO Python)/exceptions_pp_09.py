numbers = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5, 6]
numbers3 = [1, 2, 3, 4, 5, 6, 7]


#LBYL approach
# def get_sixth_element(lst):
    # if len(lst) > 5:
        # return lst[5]
    # return None

# print(get_sixth_element(numbers))
# print(get_sixth_element(numbers2))
# print(get_sixth_element(numbers3))

# AFNP approach
def get_sixth_element(lst):
    try:
        return lst[5]
    except IndexError:
        return None

print(get_sixth_element(numbers))
print(get_sixth_element(numbers2))
print(get_sixth_element(numbers3))