my_list = [0, 1234, -324, 234]
dup = list(my_list)

index = 0
result = []

while index < len(dup):
    index_2 = 1
    number = dup[index]
    while index_2 < len(dup):
        if number > dup[index_2]:
            number = dup[index_2]

        index_2 += 1
    
    result.append(number)
    dup.remove(number)


print(result) # Prints [-324, 0, 234, 1234]

print(sorted(my_list)) # Prints [-324, 0, 234, 1234]
