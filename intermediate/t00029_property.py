"""#00029  @property - methods that look like attributes (with validation)."""
class Circle:
    def __init__(self, radius):
        self.radius = radius                  # goes through the setter below

    @property
    def radius(self):                         # getter: c.radius
        return self._radius

    @radius.setter
    def radius(self, value):                  # setter: c.radius = 5
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("deleting radius"); del self._radius

    @property
    def area(self):                           # computed, read-only
        return 3.14159 * self._radius ** 2

c = Circle(3)
print(c.radius, c.area)
c.radius = 5
print(c.area)
for bad in (-1,):
    try: c.radius = bad
    except ValueError as e: print("Error:", e)
try: c.area = 10
except AttributeError as e: print("Error:", e)
del c.radius

# Why use it? Start with plain attribute, add validation LATER without changing callers.
class Temp:
    def __init__(self, celsius): self.celsius = celsius
    @property
    def fahrenheit(self): return self.celsius * 9 / 5 + 32
    @fahrenheit.setter
    def fahrenheit(self, f): self.celsius = (f - 32) * 5 / 9
t = Temp(100); print(t.fahrenheit); t.fahrenheit = 32; print(t.celsius)
