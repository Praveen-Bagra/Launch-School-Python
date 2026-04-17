def all_caps_longer_than_10(message):
    if len(message) > 10:
        return message.upper()
    else:
        return message

print(all_caps_longer_than_10('hello world'))
print(all_caps_longer_than_10('goodbye'))