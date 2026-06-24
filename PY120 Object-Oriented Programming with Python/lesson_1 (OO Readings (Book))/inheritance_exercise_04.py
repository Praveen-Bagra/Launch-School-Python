class SignalMixin:

    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')

class Vehicle:

    number_of_vehicles = 0

    def __init__(self):
        Vehicle.number_of_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.number_of_vehicles

class Car(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()
        
class Truck(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()

print(Car.mro())
print()
print(Truck.mro())
print()
print(Boat.mro())
print()
print(Vehicle.mro())
