class TireMixin:
    def set_tires(self, tires_lst):
        self.tires = tires_lst 

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Vehicle:
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class Auto(TireMixin, Vehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__(50, 25.0)
        self.set_tires([30, 30, 32, 32])

class Motorcycle(TireMixin, Vehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__(80, 8.0)
        self.set_tires([20, 20])

class Catamaran(Vehicle):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter, liters_of_fuel_capacity)
        self.propellers = number_propellers
        self.hulls = number_hulls
    
    def range(self):
        return super().range() + 10

class MotorBoat(Catamaran):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 8, 100)
motorboat = MotorBoat(10, 400)

print(auto.range())
print(motorcycle.range())
print(catamaran.range())
print(motorboat.range())