"""#00013  __repr__ -> the *developer* text of an object (unambiguous, debugging).
Rule of thumb:  str() = readable, repr() = precise.  Ideal repr looks like the code that rebuilds it.
"""
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(2, 3)
print(p)             # uses __str__  -> (2, 3)
print(repr(p))       # uses __repr__ -> Point(x=2, y=3)
print([p, p])        # containers show repr
print(f"{p!r}")      # force repr inside f-string
print(eval(repr(p))) # repr can rebuild the object

print(str("hi"), repr("hi"))             # hi  'hi'   (repr shows quotes)
import datetime
d = datetime.date(2026, 1, 1)
print(str(d), "|", repr(d))

class OnlyRepr:
    def __repr__(self): return "OnlyRepr()"
print(OnlyRepr())    # if __str__ is missing, print falls back to __repr__
