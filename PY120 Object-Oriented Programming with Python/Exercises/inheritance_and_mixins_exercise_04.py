class Vehicle:

    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):

    def start_engine(self, speed):
        if speed == 'fast':
            return 'Ready to go! Drive fast, please!'
        elif speed == 'slow':
            return 'Ready to go! Drive slow, please!'
        else:
            return 'Not valid speed.'

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!

