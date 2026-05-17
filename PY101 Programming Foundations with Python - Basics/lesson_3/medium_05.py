import math
nan_value = float("nan")

print(nan_value == float("nan")) # It will print false since it not a 
                                 # number.

print(math.isnan(nan_value))