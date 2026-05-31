import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

# The function 'copy.copy()' creates a shallow copy. The original and 
# shallow copy shares the same references for their elements. Since
# original list contains nested lists and they are mutable, we can change
# their value. We did that above so same change will be reflected in both
# the lists.