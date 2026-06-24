# class Person:

    # def __init__(self, first_name, last_name):
        # if (not first_name.isalpha()) or (not last_name.isalpha()):
            # raise ValueError('Name must be alphabetic.')

        # self._first_name = first_name
        # self._last_name = last_name

    # @property
    # def name(self):
        # return self._first_name.capitalize() + ' ' + self._last_name.capitalize()

    # @name.setter
    # def name(self, tup):
        # if not all([name.isalpha() for name in tup]):
            # raise ValueError('Name must be alphabetic.')

        # self._first_name = tup[0]
        # self._last_name = tup[1]
            
        
# actor = Person('Mark', 'Sinclair')
# print(actor.name)
# actor = Person('Vin', 'Diesel')
# print(actor.name)
# actor.name = ('', 'Diesel')

# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character.name = ('praVEEN', 'BAGRA')
# print(character.name)          # Praveen Bagra 

# friend = Person('Lynn', 'Blake')
# print(friend.name)             # Lynn Blake
# friend.name = ('Lynn', 'Blake-John')
# # ValueError: Name must be alphabetic.

class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'

    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name