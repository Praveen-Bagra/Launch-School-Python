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

    # @classmethod
    # def average(cls, distance_travelled, fuel_burned):
        # total_average = distance_travelled / fuel_burned
        # print(f'The average of the car is {total_average:.2f} miles per gallon.')
    
    @classmethod
    def gas_mileage(cls, gallons, miles):
        mileage = miles / gallons
        print(f'{mileage:.2f} miles per gallon')


lumina = Car('chevy lumina', 1997, 'white')

# Car.average(1000, 10)
Car.gas_mileage(13, 352)