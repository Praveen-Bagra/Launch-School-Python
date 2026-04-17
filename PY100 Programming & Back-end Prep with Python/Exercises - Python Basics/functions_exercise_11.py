def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    if (extract_language(locale) == 'en'
            and extract_region(locale) == 'US'):
        return 'Hey!'
    elif (extract_language(locale) == 'en'
            and extract_region(locale) == 'GB'):
        return 'Hello!'
    elif (extract_language(locale) == 'en'
            and extract_region(locale) == 'AU'):
        return 'Howdy!'
    elif extract_language(locale) == 'fr':
        return 'Salut!'
    else:
        return 'Not Found.'

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
print(local_greet('cr_MA.UTF-8'))       # Not Found.