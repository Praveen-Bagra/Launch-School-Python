for value in ['abc', '0']:
    try:
        number = float(value)
        quotient = 3.0 / number
        break
    except ValueError as e:
        print("Opps! That's not a valid number.", e, '', sep='\n')
    except ZeroDivisionError as e:
        print("Oops! You tried to divide by zero!", e, '', sep='\n')