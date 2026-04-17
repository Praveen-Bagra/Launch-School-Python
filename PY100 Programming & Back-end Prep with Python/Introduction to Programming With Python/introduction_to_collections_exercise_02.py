stuff = ('hello', 'world', 'bye', 'now')


stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)

print(stuff)

# Tuples are immutable collection type, so we can't change it's element. 
# However we can convert into list and than change it's element and then
# convert to tuple.