# input: number
# output: number
# rules:
#   explicit:
#       - Given a natural number and a set of one or more other numbers:
#           - To return a sum of all the multiples in the set that are
#             less than then the original natural number.
#           - Mulitples will be unique.
#           - If set of numbers is not given, use a default set of 3 & 5.
# Data Structure and Algorithm:
#   - Initialize multiples to empty set.
#   - Iterate for each number in the set:
#       - Iterate from 1 to original number - 1:
#           - if current number is multiple of number in set:
#               - Add current number to multiples 
#   - Return sum of multiples

class SumOfMultiples:
    def __init__(self, *numbers):
        self._numbers = set(numbers)
    
    def to(self, number):
        if not self._numbers:
            self._numbers = {3, 5}

        multiples = set()
        for num in self._numbers:
            for current_num in range(1, number):
                if current_num % num == 0:
                    multiples.add(current_num)

        return sum(multiples)

    @classmethod
    def sum_up_to(cls, number):
        return cls().to(number)