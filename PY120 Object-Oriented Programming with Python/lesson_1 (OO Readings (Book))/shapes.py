class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        my_area = self.width * self.height
        print(f'area is {my_area}')

class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)

    def set_size(self, size):
        self.width = size
        self.height = size

square = Square(7)
square.area()

square.set_size(12)
square.area()

square.width = 5
square.height = 9

square.area()