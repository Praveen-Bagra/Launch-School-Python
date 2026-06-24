# class Car:

    # def __init__(self, model, model_year, color):
        # self._model = model
        # self._model_year = model_year
        # self._color = color
        # self.current_speed = 0

    # def engine_on(self):
        # print("The car engine has been turned on...")

    # def accelerate(self):
        # print("The car is now accelerating...")
        # self.current_speed += 20

    # def brake(self):
        # print("The car has applied the brake.")
        # self.current_speed = 0

    # def engine_off(self):
        # print("The car's engine has turned off.")
        # self.current_speed = 0

    # def display_current_speed(self):
        # print(f"The current speed of the car is {self.current_speed} km per hour.")

# alto = Car('Alto', 2018, 'White')

# alto.engine_on()
# alto.display_current_speed()
# alto.accelerate()
# alto.display_current_speed()
# alto.accelerate()
# alto.display_current_speed()
# alto.brake()
# alto.display_current_speed()
# alto.accelerate()
# alto.display_current_speed()
# alto.brake()
# alto.display_current_speed()
# alto.accelerate()
# alto.display_current_speed()
# alto.engine_off()
# alto.display_current_speed()

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

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

lumina = Car('chevy lumina', 1997, 'white')
lumina.engine_start()
lumina.get_speed()
lumina.speed_up(20)
lumina.get_speed()
lumina.speed_up(30)
lumina.get_speed()
lumina.brake(15)
lumina.get_speed()
lumina.brake(30)
lumina.get_speed()
lumina.engine_off()

