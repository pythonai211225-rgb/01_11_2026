import math
from typing import override

from shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    @override
    def area(self):
        return math.pi * self._radius**2

    @property
    @override
    def perimeter(self):
        return 2 * math.pi * self._radius

    @override
    def __str__(self):
        return (f'radius={self.radius} ' + \
                super().__str__())

c = Circle("Circle_4.9", 4.9)
print(c.name)
print(c)

