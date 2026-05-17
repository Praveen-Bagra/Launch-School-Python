def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# In buffer1, it is mutataing the argument list while buffer2 is 
# creating a new list.

lst = [1, 2, 3, 4]

# print(add_to_rolling_buffer1(lst, 4, 5))
print(add_to_rolling_buffer2(lst, 4, 5))
print(lst)


