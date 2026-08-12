# def stop_generator():
    # stop = False
    # while not stop:
        # answer = input("Please enter 'stop' to exit. ")

        # yield answer
        # if answer == 'stop':
            # stop = True

# while True:
    # answer = next(stop_generator())

    # if answer == 'stop':
        # break

def input_generator():
    while True:
        s = input("Enter a string: ")
        if s == 'stop':
            break
        yield s

for user_input in input_generator():
    print(user_input)