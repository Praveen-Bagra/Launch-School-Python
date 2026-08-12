import re

class Octal:
    def __init__(self, str_num):
        self._str_num = str_num

    def to_decimal(self):
        if re.search(r'[^01234567]', self._str_num):
            return 0

        num = 0
        for idx, digit_str in enumerate(self._str_num[::-1]):
                num += int(digit_str) * (8**idx)

        return num 





        