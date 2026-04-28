# input: string number greater than 0
# output: print sum or multiplicaton from all the numbers between 1
#         and the integer provided based on the user choice
# Test Cases:
#   Entered: 5 (Sum) # 1 + 2 + 3 + 4 + 5 = Prints 15
#   Entered: 5 (Product) # 1 * 2 * 3 * 4 * 5 = Prints 120
#   Entered: 1 (Sum) # 1
#   Entered: 1 (Product) # 1
# Data Structure and Algorithm:
#   a. Ask the user for integer greater than 0. Convert it into int. 
#      Initliaze the 'number' variable pointing to it.
#   b. Ask the user for sum or product. Intialize the variable 'choice'
#      pointing to it.
#   c. Initialize the variable sum and product to 0 and 1 respectively.
#   d. Iterate over the numbers between 1 and number all inclusive.
#   e. Check the choice, if it is sum, increase the sum by adding each 
#      number in iteration and saving it to sum, and if it is product, 
#      increase the product by muliplying each number in iteration and
#      save it in product variable.
#   f. Based on the choice, print the required statment with either
#      product or sum.

number = int(input('Please enter an integer greater than 0: '))
choice = input('Enter "s" to compute the sum, '
               'or "p" to compute the product. ')
sum = 0
product = 1
for num in range(1, number+1):
    if choice == 's':
        sum += num
    elif choice == 'p':
        product *= num

print()
if choice == 's':
    print(f'The sum of the integers between 1 and {number} is {sum}.')
elif choice == 'p':
    print(f'The product for the integers between 1 and {number} is {product}.')
