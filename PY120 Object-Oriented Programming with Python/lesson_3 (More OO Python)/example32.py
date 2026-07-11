try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError
except ValueError:
    print("It worked as expected.")    