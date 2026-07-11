for divisor in [2, 0]:
    try:
        result = 10 / divisor
    except ZeroDivisionError:
        print('Division by zero!')
        raise
    else:
        print(f'Result is {result}')
    finally:
        print(f"We're done with divisor == {divisor}")