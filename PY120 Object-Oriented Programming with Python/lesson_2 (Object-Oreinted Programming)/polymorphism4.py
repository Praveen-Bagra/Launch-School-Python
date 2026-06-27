class Dog:

    def walk(self):
        print('Walking the dog.')

    def _chase_car(self):
        print('I am chasing a car!')

    def __goto_vet(self):
        print('The vet! Run and hide!')

    def a_day_in_the_life(self):
        self.walk()
        self._chase_car()
        self.__goto_vet()

rover = Dog()

rover.a_day_in_the_life()

rover.walk()
rover._chase_car()
rover._Dog__goto_vet()
rover.__goto_vet()