# input: 2 objects
# output: Returns True if exactly one of its arguments is truthy
# Test Cases:
#   print(xor(5, 0) == True)
#   print(xor(False, True) == True)
#   print(xor(1, 1) == False)
#   print(xor(True, True) == False)
# Data Structure and Algorithm:
#   a. Initialize result = false
#   b. Check if obj1 has truthy value
#       result = true
#           if obj2 has truthy value
#               result = false
#       elif obj2 has truthy value
#         result = true
#           if obj1 has truthy value
#               result = false
#   c. Return the result

def xor(obj1, obj2):
    result = False
    if obj1:
        result = True
        if obj2:
            result = False
    elif obj2:
        result = True
        if obj1:
            result = False
    
    return result

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

        