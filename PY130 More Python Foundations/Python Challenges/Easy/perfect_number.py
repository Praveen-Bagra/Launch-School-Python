# input: number
# output: string
# rules:
#   explicit:
#       - The input will be a natural number i.e. 1, 2, 3,....
#       - To return the category of this number
#           - Abundant: If sum of its positive divisiors is greater
#                       than the original number.
#           - Deficient: If sum of its positive divisiors is less
#                        than the original number.
#           - Perfect: If sum of its positive divisors is equsl to
#                      the original number.
#       - Positive Divisiors doesn't include the original number.
#   implicit:
#       - If input is invalid, raise respective error.
# Data Structure and Algorithm:
#   - If aliquot sum is greater than original number:
#       - return Abundant
#   - If aliquot sum is less than original number:
#       - return Deficient 
#   - return Perfect

#   FUNCTION aliquot sum:
#   - Initialize positive_divisors to [1]. 
#     Since natural number will always be divisible by 1.
#   - Iterate from 2 to original number - 1. 
#           - If original number is divisible by current number
#             and remainder is 0
#                   - add current num to positive_divisors 

class PerfectNumber:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError("Not a valid natural number.")

        if number <= 0:
            raise ValueError("Input must be a positive integer")
        
        self._number = number

    def category(self):
        if self._aliquot_sum() > self.number:
            return 'abundant'
        
        if self._aliquot_sum() < self.number:
            return 'deficient'

        return 'perfect'

    def _aliquot_sum(self):
        positive_divisors = [1] # Will always be divisible by 1.

        for num in range(2, self.number):
            current_num = num
            if self.number % current_num == 0:
                positive_divisors.append(current_num)

        return sum(positive_divisors)
    
    @classmethod
    def classify(cls, number):
        return cls(number).category()
             
            

