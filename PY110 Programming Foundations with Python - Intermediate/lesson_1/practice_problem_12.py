frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6) 
# The above code will raise an exception AttributeError since
# frozensets are immutable. There is no such method available for
# frozensets.
print(frozen)

