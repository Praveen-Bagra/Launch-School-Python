# input: Two float numbers
# output: Multiple strings of addtion, subtraction, product,etc
# Test Cases:
    # ==> Enter the first number:
    # 3.141592
    # ==> Enter the second number:
    # 2.718282
    # ==> 3.141592 + 2.718282 = 5.859874
    # ==> 3.141592 - 2.718282 = 0.4233100000000003
    # ==> 3.141592 * 2.718282 = 8.539732984944001
    # ==> 3.141592 / 2.718282 = 1.1557270364149121
    # ==> 3.141592 // 2.718282 = 1.0
    # ==> 3.141592 % 2.718282 = 0.4233100000000003
    # ==> 3.141592 ** 2.718282 = 22.45914942746313
# Data Structure and Algorithm:
#   a. Do the operation and print strings.

# print('==> Enter the first number: ')
# first_number = float(input())
# print('==> Enter the second number: ')
# second_number = float(input())

# print(f'==> {first_number} + {second_number} = ' 
      # f'{first_number + second_number} ')
# print(f'==> {first_number} - {second_number} = ' 
      # f'{first_number - second_number} ')
# print(f'==> {first_number} * {second_number} = ' 
      # f'{first_number * second_number} ')
# print(f'==> {first_number} / {second_number} = ' 
      # f'{first_number / second_number} ')
# print(f'==> {first_number} // {second_number} = ' 
      # f'{first_number // second_number} ')
# print(f'==> {first_number} % {second_number} = ' 
      # f'{first_number % second_number} ')
# print(f'==> {first_number} ** {second_number} = ' 
      # f'{first_number ** second_number} ')

def calculate(first_number, second_number, operator):
    match operator:
        case '+': return first_number + second_number
        case '-': return first_number - second_number
        case '*': return first_number * second_number
        case '/': return first_number / second_number
        case '//': return first_number // second_number
        case '%': return first_number % second_number
        case '**': return first_number ** second_number

first_number = float(input('==> Enter the first number:\n'))
second_number = float(input('==> Enter the second number:\n'))

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f'{first_number} {operator} {second_number}'
    result = calculate(first_number, second_number, operator)
    print(f'==> {operation} = {result}')