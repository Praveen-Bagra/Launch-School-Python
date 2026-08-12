class Triangle():
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

        self._sides = (self._side1, self._side2, self._side3)

        if not self._is_valid():
            raise ValueError("Invalid triangle lengths")

    @property
    def kind(self):
        if self._side1 == self._side2 == self._side3:
            return 'equilateral'

        if ((self._side1 == self._side2) or
           (self._side1 == self._side3) or
           (self._side2 == self._side3)):
            return 'isosceles'

        return 'scalene' 

    def _is_valid(self):
        for side in self._sides:
            if side <= 0:
                return False

        if (((self._side1 + self._side2) <= self._side3) or 
          ((self._side1 + self._side3) <= self._side2) or
          ((self._side2 + self._side3) <= self._side1)):
            return False

        return True 
                            