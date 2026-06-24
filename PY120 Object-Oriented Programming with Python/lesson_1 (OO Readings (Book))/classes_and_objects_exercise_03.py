class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color # Uses color setter
        self.speed = 0

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def engine_start(self):
        print('The engine is on!')

    def engine_off(self):
        self.speed = 0
        print("Let's park the baby!")
        print('The engine if off!')

    def speed_up(self, number):
        self.speed += number
        print(f'You accelerated {number} mph.')

    def brake(self, number):
        self.speed -= number
        print(f'You decelerated {number} mph.')

    def get_speed(self):
        print(f'Your speed is {self.speed} mph.')

    def spray_paint(self, color):
        self.color = color
        print(f'Your {color} paint job looks great!')

lumina = Car('chevy lumina', 1997, 'white')
lumina.spray_paint('black')
