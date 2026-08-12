def find_person(**kwargs):
    # for name, profession in kwargs.items():
        # if name == 'Antonina':
            # print(f"Antonina's profession is {profession}.")
            # return

    # print("Antonina not found.")

    if 'Antonina' in kwargs:
        print(f"Antonina's profession is {kwargs['Antonina']}.")
    else:
        print("Antonina not found.")


find_person(John='Electrician', Bob='Plumber')
find_person(John='Electrician', Bob='Plumber', Antonina='Software Engineer')
