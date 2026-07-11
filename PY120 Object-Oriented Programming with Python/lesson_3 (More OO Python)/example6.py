class SmartLamp:
    def __init__(self, color):
        self.color = color

    def glow(self):
        return (f'The lamp glows {self.color}.')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("Color must be a color name.")

        self._color = color

lamp = SmartLamp('blue')
print(lamp.color)
print(lamp.glow())

lamp.color = 'red'
print(lamp.color)
print(lamp.glow())

# lamp.color = 12345
lamp1 = SmartLamp(12345)
