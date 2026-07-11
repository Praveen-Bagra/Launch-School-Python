number = None
while True:
    number = input('Please enter a number: ')
    try:
        number = float(number)
        break
    except ValueError:
        print("Oops! That's not a valid number. Try again. \n")

print(f'Thanks! You entered {number}.')