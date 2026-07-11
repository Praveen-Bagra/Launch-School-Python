class Person:
    name = 'Leslie'

    @classmethod
    def get_name(cls):
        return [cls.name, Person.name]

class Teacher(Person):
    name = 'Ms Taylor'

print(Person.get_name())
print(Teacher.get_name())