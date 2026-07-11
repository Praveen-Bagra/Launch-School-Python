for divisor in [2, 0]:
    try:
        result = 10 / divisor
    except ZeroDivisionError as e:
        print('Division by zero!')
    else:
        print(f'Result is {result}')