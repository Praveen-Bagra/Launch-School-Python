# input: string
# output: string
# rules:
#   Explicit:
#       To check whether the sixth number is in the first five numbers.
# Test Cases:
#   1:
#       Enter the 1st number: 25
#       Enter the 2nd number: 15
#       Enter the 3rd number: 20
#       Enter the 4th number: 17
#       Enter the 5th number: 23
#       Enter the last number: 17

        # 17 is in 25,15,20,17,23.
#   2:
#       Enter the 1st number: 25
#       Enter the 2nd number: 15
#       Enter the 3rd number: 20
#       Enter the 4th number: 17
#       Enter the 5th number: 23
#       Enter the last number: 18

#       18 isn't in 25,15,20,17,23.
# Data Structure/ Algorithm
#   - Initialize variable iteration_str to ['1st', '2nd', '3rd', '4th', '5th'].
#   - Intialized variable nums to empty list.
#   - Iterate over iteration_str:
#       print required prompt and ask for the number and append that
#       to the nums list. 
#   - Ask for the last number.
#   - Check if it is in the nums list, 
#       - if yes, print sixth number in nums list (print numbers)
#       - if no, print sixth numbers isn't in nums list (print numbers)

iteration_str = ['1st', '2nd', '3rd', '4th', '5th']
nums = []

for iteration in iteration_str:
    num = int(input(f'Enter the {iteration} number: '))
    nums.append(num)

last_number = int(input('Enter the last number: '))

if last_number in nums:
    print(f'{last_number} is in {','.join([str(num) for num in nums])}.')
else:
    print(f"{last_number} isn't in {','.join([str(num) for num in nums])}.")

