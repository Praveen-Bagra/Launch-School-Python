class Car:

    def __init__(self, name):
        self.name = name
        print(f'{name} is a fantastic car.')

    def move(self):
        print(f'{self.name} {self.__class__.__name__.lower()} moves wroooommmm!!!')

range_rover = Car('Range Rover')
maruti_swift = Car('Maruti Swift')

range_rover.move()
maruti_swift.move()