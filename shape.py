from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"[Shape] name: {self.name} area: {self.area} perimeter: {self.perimeter}"

# s = Shape('amorphi')  # ERROR