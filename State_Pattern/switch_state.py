
from abc import ABC, abstractmethod

class SwitchState(ABC):
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        @abstractmethod
        def turn_on(self):
            ...

        @abstractmethod
        def turn_off(self):
            ...

        @abstractmethod
        def fix(self):
            ...

        def __str__(self):
            return f"[Switch] {self._name}"