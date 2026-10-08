"""#00023  Abstraction - hide HOW, expose WHAT. Python tool: abc module."""
from abc import ABC, abstractmethod
import math

class Shape(ABC):                         # abstract base class
    @abstractmethod
    def area(self): ...                   # every child MUST implement this
    @abstractmethod
    def perimeter(self): ...
    def describe(self):                   # normal (concrete) method is allowed
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r

class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

try:
    Shape()
except TypeError as e:
    print("Error:", e)

class Broken(Shape):                      # forgot perimeter()
    def area(self): return 0
try:
    Broken()
except TypeError as e:
    print("Error:", e)

for s in (Circle(2), Rect(3, 4)):         # caller only knows 'Shape', not details
    print(s.describe())
