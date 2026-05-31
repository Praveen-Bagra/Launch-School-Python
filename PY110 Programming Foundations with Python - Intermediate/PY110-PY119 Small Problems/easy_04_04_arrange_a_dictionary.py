def order_by_value(dictionary):
    def value_key(key):
        return dictionary[key]

        keys = list(dictionary.keys())

    return sorted(keys, key=value_key)

# def sort_key(tup):
    # return tup[1]

# def order_by_value(d):
    # sorted_items = sorted(d.items(), key=sort_key)
    # return [key for key, _ in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
    
