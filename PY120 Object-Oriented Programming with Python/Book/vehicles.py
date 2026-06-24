class Vehicle:

    def drive(self):
        print('I am driving.')

class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass

class Motorcycle(Vehicle):

    def drive(self):
        super().drive()
        print('   No! I am riding!')

car = Car()
car.drive()

truck = Truck()
truck.drive()

motorcycle = Motorcycle()
motorcycle.drive()