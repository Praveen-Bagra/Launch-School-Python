d = {
    'a': 1,
    'b': 2,
    'c': 3
}

def list_of_tuples(d):
    result = []
    for key in d:
        result.append((key, d[key]))

    return result


print(list_of_tuples(d))