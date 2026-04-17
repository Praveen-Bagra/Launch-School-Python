def compare_by_length(first_str, second_str):
    if len(first_str) > len(second_str):
        return 1
    elif len(second_str) > len(first_str):
        return -1
    else:
        return 0

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity')     ) #  1
print(compare_by_length('humor', 'grace')          ) #  0