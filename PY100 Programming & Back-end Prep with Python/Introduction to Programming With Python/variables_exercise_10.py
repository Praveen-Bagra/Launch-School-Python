obj = 42 # Initialized a variable named 'obj' to int object 42
obj = 'ABcd' # Reassigned a variable named 'obj' to new str object 'ABcd'
obj.upper() # Neither 
obj = obj.lower() # Reassigned a variable named 'obj' to new str object 'abcd'
print(len(obj)) # Neither. Display total characters in a string i.e. 4
obj = list(obj) # Reassigned a variable name 'obj' to new list ojbect
#                 ['a', 'b', 'c', 'd']
obj.pop() # Removed and returned the last element from the 'obj' list. 
#           Mutated the list to ['a', 'b', 'c'] that variable 'obj' was
#           referencing 
obj[2] = 'X'# Mutated the 'obj' list to ['a', 'b', 'X']
obj.sort() # Mutated the 'obj' list to ['X', 'a', 'b']
set(obj) # Neither
obj = tuple(obj) # Reassigned a new tuble object ('X', 'a', 'b') to variable
#                  named 'obj'
print(obj)