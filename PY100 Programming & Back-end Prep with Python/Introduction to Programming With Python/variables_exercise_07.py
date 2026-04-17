NAME = 'Victor' # We're initializing a constant here. Since variable name is
#                 in all uppercase.

print('Good Morning, ' + NAME) # Will display: Good Morning, Victor
print('Good Afternoon, ' + NAME) # Will display: Good Afternoon, Victor
print('Good Evening, ' + NAME) # Will display: Good Evening, Victor

NAME = 'Nina' # We are reassigning constant 'NAME' to a new string object 
#               'Nina', which is a poor practice. We shouldn't reassign
#               constants.


print('Good Morning, ' + NAME) # Will display: Good Morning, Nina
print('Good Afternoon, ' + NAME) # Will display: Good Afternoon, Nina
print('Good Evening, ' + NAME) # Will display: Good Evening, Nina