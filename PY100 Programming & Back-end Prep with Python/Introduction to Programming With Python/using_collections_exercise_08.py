text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 It applies str.rfind('f') on string 
# 'for the fjords' thats why returns 8. rfind searches from the right for the
# first occurance of that character/substring
print(text.rfind('f', 21, 35))    # 29 Starting index is considered hence it
# returns 29