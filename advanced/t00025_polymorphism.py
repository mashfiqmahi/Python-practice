"""#00025  Polymorphism = same call, different behavior.

Python has NO compile-time overloading (it's interpreted & dynamic).
 - Overriding   -> RUN-time polymorphism (child replaces parent method)   [real]
 - Overloading  -> COMPILE-time in Java/C++; in Python we SIMULATE it
"""
# ---------- 1) Method overriding (run-time) ----------
class Animal:
    def speak(self): return "..."
class Dog(Animal):
    def speak(self): return "Woof"
class Cat(Animal):
    def speak(self): return "Meow"
for a in (Animal(), Dog(), Cat()):
    print(type(a).__name__, "->", a.speak())     # decided at RUN time by the real object

# ---------- 2) Duck typing: "if it quacks like a duck..." (no inheritance needed) ----------
class Robot:
    def speak(self): return "Beep"
print([x.speak() for x in (Dog(), Robot())])

# ---------- 3) Method overloading: Python keeps only the LAST definition ----------
class Calc:
    def add(self, a, b): return a + b
    def add(self, a, b, c): return a + b + c    # silently REPLACES the first!
try: Calc().add(1, 2)
except TypeError as e: print("Error:", e)

# Simulation A: default / variable arguments
class Calc2:
    def add(self, *nums): return sum(nums)
print(Calc2().add(1, 2), Calc2().add(1, 2, 3, 4))

# Simulation B: check the type
class Show:
    def show(self, x):
        if isinstance(x, int): return f"int {x}"
        if isinstance(x, str): return f"str {x}"
        return f"other {x}"
print(Show().show(1), Show().show("a"))

# Simulation C: functools.singledispatch (real dispatch on type)
from functools import singledispatch
@singledispatch
def describe(x): return f"generic {x}"
@describe.register(int)
def _(x): return f"int {x}"
@describe.register(list)
def _(x): return f"list of {len(x)}"
print(describe(5), describe([1, 2]), describe(2.5))

# ---------- 4) Operator overloading (built-in polymorphism) ----------
print(1 + 2, "a" + "b", [1] + [2], len("abc"), len([1, 2]))
class Money:
    def __init__(self, v): self.v = v
    def __add__(self, o): return Money(self.v + o.v)
    def __repr__(self): return f"Money({self.v})"
print(Money(5) + Money(7))
