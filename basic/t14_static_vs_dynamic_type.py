"""#00014  Static typing vs dynamic typing (and strong vs weak).

Static  (Java, C++): variable has a fixed type declared up front -> `int x = 5;`
Dynamic (Python)   : the VALUE has a type; the NAME can point to anything.
Python is dynamic + STRONG: it will not silently mix incompatible types.
"""
x = 5;        print(type(x))
x = "five";   print(type(x))      # fine in Python

try:
    print("5" + 5)                # strong typing: no silent conversion
except TypeError as e:
    print("Error:", e)
print("5" + str(5), int("5") + 5)

# Type hints = documentation + tool support. Python does NOT enforce them at runtime.
def double(n: int) -> int:
    return n * 2
print(double("ab"))               # works anyway -> 'abab'
print(double.__annotations__)

# Check types at runtime yourself
def safe_double(n):
    if not isinstance(n, (int, float)):
        raise TypeError("number required")
    return n * 2
print(safe_double(4))
print(isinstance(True, int), type(True) is int)   # bool is a subclass of int!

# For static checking run:  pip install mypy  ->  mypy this_file.py
from typing import Optional
def find(name: str) -> Optional[int]:
    return {"a": 1}.get(name)
print(find("a"), find("z"))
