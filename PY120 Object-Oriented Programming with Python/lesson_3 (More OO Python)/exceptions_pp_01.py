try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f'The result is: {result}')
except ValueError:
    print("Please enter valid numbers!") 
except ZeroDivisionError:
    print("Cannot divide by zero!")