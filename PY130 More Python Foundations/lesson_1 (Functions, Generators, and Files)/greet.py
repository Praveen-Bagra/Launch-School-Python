# def greet(language):
    # match language:
        # case 'en':
            # print('Hello!')
        # case 'es':
            # print('Hola!')
        # case 'fr':
            # print('Bonjour!')

# greet('fr')
# greet('es')

def create_greeter(language):
    match language:
        case 'en':
            return lambda: print('Hello')
        case 'es':
            return lambda: print('Hola!')
        case 'fr':
            return lambda: print('Bonjour!')

es_greeter = create_greeter('es')
es_greeter()
es_greeter()
es_greeter()

en_greeting = create_greeter('en')
en_greeting()