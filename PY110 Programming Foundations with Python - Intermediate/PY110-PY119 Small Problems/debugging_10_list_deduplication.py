data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))
unique_data = list({value: key for key, value in enumerate(data)})
print(unique_data)
print(unique_data == [4, 2, 1, 3]) # order not guaranteed