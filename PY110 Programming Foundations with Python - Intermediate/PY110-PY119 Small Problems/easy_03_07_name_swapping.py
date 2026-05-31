def swap_name(full_name):
    # first_name, last_name = full_name.split()
    # return f'{last_name}, {first_name}'
    
    return ', '.join(full_name.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True