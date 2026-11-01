from typing import override

from four_sides import FourSides

class Rectangle(FourSides):
    def __init__(self, name, a, b):
        super().__init__(name, a=a, b=b, c=a, d=b)
        self._name = 'Rectangle'

    @property
    @override
    def area(self):
        return self._a * self._b

    @property
    @override
    def perimeter(self):
        return (self._a + self._b) * 2

    def __str__(self):
        return "[Rectangle]" + super().__str__()