dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

new_list = []

for fruit_details in dict1.values():
    if fruit_details['type'] == 'fruit':
        new_sublist = []

        for color in fruit_details['colors']:
            new_sublist.append(color.capitalize()) 

        new_list.append(new_sublist)
    else:
        new_list.append(fruit_details['size'].upper())

print(new_list)

new_list = [([color.capitalize() for color in fruit_info['colors']]
            if fruit_info['type'] == 'fruit' else fruit_info['size'].upper())
            for fruit_info in dict1.values()]

print(new_list)