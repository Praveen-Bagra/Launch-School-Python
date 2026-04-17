counter = 0

while counter < 5:
    print(counter)

# The problem occured in the loop body. It caused an infinte loop because the 
# condition in the while loop (counter < 5) always remained truthy. 
# We never incremented the counter. 