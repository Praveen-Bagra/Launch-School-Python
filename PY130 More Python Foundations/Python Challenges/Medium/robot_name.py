# import random

# class Robot:
    # LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # DIGITS = '0123456789'
    # _names = set()

    # def __init__(self):
        # self._set_name()

    # @property
    # def name(self):
        # return self._name

    # def _set_name(self):
        # while True:
            # chars = (random.choices(Robot.LETTERS, k=2)
                        # + random.choices(Robot.DIGITS, k=3))
            # name = ''.join(chars)

            # if name in Robot._names:
                # continue
            
            # Robot._names.add(name)
            # break

        # self._name = name

    # def reset(self):
        # self._names.discard(self._name)
        # self._set_name()

# robot1 = Robot()
# robot2 = Robot()
# robot3 = Robot()

# print(robot1.name)
# print(robot2.name)
# print(robot3.name)
# print(Robot._names)

# robot1.reset()
# print()
# print(robot1.name)
# print(Robot._names)

import random

class Robot:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    DIGITS = '0123456789'
    # _names = set()

    def __init__(self):
        self._set_name()

    @property
    def name(self):
        return self._name

    def _set_name(self):
        chars = (random.choices(Robot.LETTERS, k=2)
                        + random.choices(Robot.DIGITS, k=3))
        name = ''.join(chars)

        self._name = name

    def reset(self):
        self._set_name()