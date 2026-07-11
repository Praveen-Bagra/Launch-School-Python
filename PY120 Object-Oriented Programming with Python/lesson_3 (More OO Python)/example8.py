import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        print(f'Getting radius value {self._radius}.')
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative.')
        print(f'Setting radius value = {value}.')
        self._radius = value