class Transform:
    def __init__(self, string):
        self._string = string

    def uppercase(self):
        return self._string.upper()
    
    # @classmethod
    # def lowercase(cls, str_):
        # return str_.lower()

    @staticmethod
    def lowercase(str_):
        return str_.lower()


my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
