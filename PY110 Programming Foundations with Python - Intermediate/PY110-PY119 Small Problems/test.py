def names_youngest_to_oldest(people):
    names = list(people.keys())
    
    def age_key(name):
        return people[name]

    names.sort(key=age_key)
    return names

# Test Cases
people_1 = {'jim': 50, 'jill': 25, "artemis": 42, 'johnny': 37, 'earl': 65}
people_2 = {'alexandra': 5, 'bob': 94, "jolene": 44, 'demosthenes': 26}
people_3 = {'sigmund': 10, 'jane': 21, "colin": 17}

print(names_youngest_to_oldest(people_1) == ['jill', 'johnny', 'artemis', 'jim', 'earl'])
print(names_youngest_to_oldest(people_2) == ['alexandra', 'demosthenes', 'jolene', 'bob'])
print(names_youngest_to_oldest(people_3) == ['sigmund', 'colin', 'jane'])
