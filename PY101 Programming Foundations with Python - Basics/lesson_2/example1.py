try:
    number = int(input("Enter a number to divide 10 by: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print(f"The result is {result}")
finally:
    print("Execution of the try-except block is complete.")
