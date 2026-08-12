from dataclasses import dataclass

@dataclass
class Square:
    width: float

    @property
    def area(self):
        return self.width**2