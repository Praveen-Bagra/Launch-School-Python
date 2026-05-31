def get_key_value(my_dict, key):
    # if key in my_dict:
        # return my_dict[key]
    # else:
        # return None
    
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))

# The expression my_dict[key] will raise an key error if there is no such
# key in the dictionary. Alsom, it it returns a falsy value, the if block
# won't execute, the else block will be executed and will return None instead
# of any falsy value.
