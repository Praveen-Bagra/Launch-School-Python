class SmartLamp:
    def __init__(self, color):
        self._color = color

    def glow(self):
        return (f'The lamp glows {self._color}.')

    def color(self):
        return self._color

    def set_color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError('Color must be a color name.')
        
        self._color = new_color

lamp = SmartLamp('blue')
print(lamp.color())
print(lamp.glow())

lamp.set_color('red')
print(lamp.color())
print(lamp.glow())

lamp.set_color(12345)