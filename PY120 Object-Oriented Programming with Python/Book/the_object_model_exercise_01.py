class Car:

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} moves wrooommmm....')

brio = Car('Honda Brio')
amaze = Car('Honda Amaze')

brio.move()
amaze.move()