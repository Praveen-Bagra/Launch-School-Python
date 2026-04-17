def multiply(number1, number2):
    return number1 * number2

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

num1 = get_number('Enter the first number: ')
num2 = get_number('Enter the second number: ')
product = multiply(num1, num2)
print(f'{num1} * {num2} = {product}')