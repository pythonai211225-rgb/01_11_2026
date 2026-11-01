from typing import override

from Four_Sides.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, a):
        super().__init__(name, a=a, b=a)

    @property
    @override
    def area(self):
        return self._a ** 2

    @property
    @override
    def perimeter(self):
        return self._a * 4

    def __str__(self):
        return "[Square]" + super().__str__()