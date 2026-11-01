from typing import override

from shape import Shape
from abc import ABC, abstractmethod

class FourSides(Shape, ABC):
    def __init__(self, name, a, b, c, d):
        super().__init__(name)
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @override
    def perimeter(self):
        return self._a + self._b + self._c + self._d

    def __str__(self):
        return f"[Four sides] a:{self._a} b:{self._b} c:{self._c} d:{self._d} " +\
            super().__str__()


