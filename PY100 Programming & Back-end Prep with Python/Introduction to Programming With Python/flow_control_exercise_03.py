def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
# It should print 'Product2' in the console.

bar_code_scanner(142)
# It should print 'Product not found!' since we are passing integer 142 as an
# argument and not string.