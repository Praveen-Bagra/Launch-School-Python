# class NegativeNumberError(Exception):
    # def __init__(self, msg="Negative numbers are not allowed!"):
        # super().__init__(msg)

class NegativeNumberError(ValueError):
    pass
    
num = float(input("Please enter a number: "))

if num < 0:
    raise NegativeNumberError("Negative numbers are not allowed!")

print(f"You entered {num}.")

