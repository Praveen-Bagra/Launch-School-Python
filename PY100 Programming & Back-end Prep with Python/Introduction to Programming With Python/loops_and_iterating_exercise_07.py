my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(things):
   return [ thing 
            for thing in things 
            if type(thing) is int ] 

integers = find_integers(my_tuple)
print(integers)