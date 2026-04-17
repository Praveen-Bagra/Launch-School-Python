grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# index = 0
# while index < len(grocery_list):
    # item = grocery_list[index]
    # print(item)
    # grocery_list.remove(item)

while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)

print(grocery_list)
