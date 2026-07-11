class Vehicle:
    WHEELS = 4

    @classmethod
    def wheels(cls):
        return Vehicle.WHEELS

class Motorcycle(Vehicle):
    WHEELS = 2

    @classmethod
    def vehicle_wheels(cls):
        return cls.WHEELS

    @classmethod
    def motorcycle_wheels(cls):
        return Motorcycle.WHEELS

print(Motorcycle.wheels())
print(Motorcycle.WHEELS)
print(Vehicle.wheels())
print(Vehicle.WHEELS)
print(Motorcycle.vehicle_wheels())
print(Motorcycle.motorcycle_wheels())