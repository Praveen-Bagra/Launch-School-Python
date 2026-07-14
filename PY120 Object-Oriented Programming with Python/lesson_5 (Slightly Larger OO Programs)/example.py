class HireAndFireMixin:
    def hire(self):
        print(f'{self.name} is hiring.')

    def fire(self):
        print(f'{self.name} is firing.')

class DelegateMixin:
    def delegate(self):
        print(f'{self.name} is delegating.')

class Employee:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number

    def __str__(self):
        return (f'Name: {self.name} \n'
                f'Type: {self.type} \n'
                f'Serial number: {self.serial_number} \n'
                f'Vacation days: {self.vacation_days} \n'
                f'Desk: {self.desk}')
        
class FullTimeEmployee(Employee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number) 

    def take_vacation(self):
        print(f'{self.name} is taking vacation.') 

class Executive(HireAndFireMixin, DelegateMixin, FullTimeEmployee):
    def __init__(self, name, serial_number):
        self.vacation_days = 20
        self.desk = 'corner officer'
        self.type = 'Executive'
        super().__init__(name, serial_number)

class Manager(DelegateMixin, FullTimeEmployee):
    def __init__(self, name, serial_number):
        self.vacation_days = 14
        self.desk = 'private office'
        self.type = 'Manager'
        super().__init__(name, serial_number)

class RegularEmployee(FullTimeEmployee):
    def __init__(self, name, serial_number):
        self.vacation_days = 10
        self.desk = 'cubile farm'
        self.type = 'Regular employee'
        super().__init__(name, serial_number)
    
class PartTimeEmployee(Employee):
    def __init__(self, name, serial_number):
        self.vacation_days = 0
        self.desk = 'open workspace'
        self.type = 'Part-time employee'
        super().__init__(name, serial_number)

dave = Manager('Dave', 123456789)
print(dave)

# Name: Dave 
# Type: Manager 
# Serial number: 123456789 
# Vacation days: 14 
# Desk: private office
