# lst = ['hello', 2 , 0, 10]

# for value in lst:
    # try:
        # inverse = 1 / value 
    # except TypeError:
        # print("Not a valid number.")
    # except ZeroDivisionError:
        # print("Can't divide by 0.")
    # else:
        # print(f"The inverse is {inverse}")

def invert_numbers(numbers):
    result = []
    for num in numbers:
        try:
            result.append(1 / num)
        except ZeroDivisionError:
            result.append(float('inf'))

    return result

numbers = [1, 2, 0, 3, 4]
print(invert_numbers(numbers))