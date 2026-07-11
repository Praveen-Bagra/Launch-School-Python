class Person:
    name = 'Leslie'

    def get_name(self):
        self.__class__.surname = 'Uriarte'
        return [
            Person.name,
            self.__class__.name,
            type(self).name,
            self.name,
        ]

class Teacher(Person):
    name = 'Ms Taylor'

teacher = Teacher()
print(teacher.get_name())

Teacher.pet = 'fido'
print(Teacher.pet)