class RomanNumeral:
    ONES = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    TENS = {0: '', 1: 'X', 2: 'XX', 3:'XXX', 4: 'XL', 5: 'L',
            6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    HUNDREDS = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D',
                6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
    THOUSANDS = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}

    ROMAN_NUMBERS = (THOUSANDS, HUNDREDS, TENS, ONES)


    def __init__(self, number):
        self._number = number

    def to_roman(self):
        ones = None
        tens = None
        hundreds = None
        thousands = None

        number = self._number

        if number <= 9:
            ones = number
            number = None
        else:
            ones = number % 10
            number = number // 10

        if number is not None:
            if number <= 9:
                tens = number
                number = None
            else:
                tens = number % 10
                number = number // 10

        if number is not None:
            if number <= 9:
                hundreds = number
                number = None
            else:
                hundreds = number % 10
                number = number // 10
        
        if number is not None:  
                thousands = number

        roman_number_string = '' 
        number_places_lst = [thousands, hundreds, tens, ones]
        for idx, number in enumerate(number_places_lst):
            if number is not None:
                roman_number_string += RomanNumeral.ROMAN_NUMBERS[idx][number]

        return roman_number_string