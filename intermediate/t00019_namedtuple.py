"""#00019  namedtuple = tuple with field names (lightweight, immutable class)."""
from collections import namedtuple
from typing import NamedTuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p, p.x, p[1])                  # access by name OR index
x, y = p; print(x, y)                # still unpacks like a tuple
print(p._asdict())                   # -> dict
p2 = p._replace(x=10); print(p2)     # immutable => _replace returns a NEW one
print(Point._fields, Point._make([7, 8]))
try:
    p.x = 5
except AttributeError as e:
    print("Error:", e)

# Defaults
Student = namedtuple("Student", "name roll gpa", defaults=[0.0])
print(Student("Nila", 7))

# Modern, typed version (supports methods + docstrings)
class Employee(NamedTuple):
    name: str
    salary: int = 30000
    def bonus(self):
        return self.salary * 0.1
e = Employee("Rahim")
print(e, e.bonus())

# Usable as dict key, sortable, tiny memory
pts = [Point(2, 1), Point(1, 5)]
print(sorted(pts), {Point(1, 1): "origin-ish"})
