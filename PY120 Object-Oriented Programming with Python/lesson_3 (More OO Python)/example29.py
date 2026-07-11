my_list = [1, 2, 3]

try:
    my_list[3]
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')