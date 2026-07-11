log_file = open("log_file.txt", "w")

try:
    open("no_such_file.txt", "r")
except OSError as e:
    print(f'{e.errno=}, {e.strerror=}, {e.filename=}', file = log_file)
    log_file.close()
    raise