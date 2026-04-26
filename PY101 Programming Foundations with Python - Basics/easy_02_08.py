# input: list that may contain 0 or more elements.
# output: Return a new list that contain 1st, 3rd, 5th, and 
#         so on elements
# Test Cases:
#   print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
#   print(oddities([1, 2, 3, 4]) == [1, 3])        # True
#   print(oddities(["abc", "def"]) == ['abc'])     # True
#   print(oddities([123]) == [123])                # True
#   print(oddities([]) == [])                      # True
# Data Structure and Algorithm:
#   a. Initilize the result = []
#   b. set counter = 1
#   c. Iterate over the argument list elements:
#       i. if counter is odd, append the element to result
#       ii. Increase the counter by 1
#   d. Return the list.

# def oddities(lst):
    # result = []
    # counter = 1
    # for element in lst:
        # if counter % 2 != 0:
            # result.append(element)
        # counter += 1
    # return result

def oddities(lst):
    return lst[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True