class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
    
    @staticmethod
    def engine_start():
        print('The engine is on!')

    def engine_off(self):
        self.speed = 0
        print("Let's park this baby!")
        print('The engine is off!')

    def speed_up(self, number):
        self.speed += number
        print(f'You accelerated {number} mph.')

    def brake(self, number):
        self.speed -= number
        print(f'You decelerated {number} mph.')

    def get_speed(self):
        print(f'Your speed is {self.speed} mph.')

lumina = Car('chevy lumina', 1997, 'white')
Car.engine_start()