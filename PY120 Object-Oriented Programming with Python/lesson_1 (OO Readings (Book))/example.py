class Vehicle:
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

car = Car()
print(isinstance(car, Car))
print(isinstance(car, Vehicle))
print(isinstance(car, Truck))

truck = Truck ()
print(isinstance(truck, Vehicle))
print(isinstance(truck, Car))
asdf