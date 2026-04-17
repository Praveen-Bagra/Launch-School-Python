def naturalNumbers(n):
    result_list = [0] * n
    for number in range(0, n):
        result_list[number] = number + 1
    return result_list

print(naturalNumbers(5))