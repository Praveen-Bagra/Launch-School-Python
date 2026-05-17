munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_male_age = 0
for name, info in munsters.items():
    if info['gender'] == 'male':
        total_male_age += info['age']

print(total_male_age)

male_ages = [info['age'] for name, info in munsters.items()
                         if info['gender'] == 'male']
total_male_age = sum(male_ages)
print(total_male_age)
